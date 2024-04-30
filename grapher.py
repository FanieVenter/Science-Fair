import matplotlib.animation as animation
import serial
import csv
from matplotlib import pyplot as plt

# Initialize serial port
ser = serial.Serial('/dev/tty.usbmodem14101', 9600, timeout=1)

if ser.is_open:
    print("\nAll right, serial port now open. Configuration:\n")
    print(ser, "\n")  # Print serial parameters

# Create figure for plotting
fig, ax = plt.subplots()

# Initialize the plot lines
line_exp, = ax.plot([], [], label="Experimental Probability")
line_theo, = ax.plot([], [], label="Theoretical Probability")

# Set up the plot formatting
ax.set_title('Thrust Over Time')
ax.set_xlabel('Time')
ax.set_ylabel('Thrust')
ax.legend()

# Initialize data lists
xs = []
ys = []
rs = []

# Open a CSV file for writing
with open('thrust_data.csv', 'w', newline='') as csvfile:
    csvwriter = csv.writer(csvfile)
    csvwriter.writerow(['Time', 'Thrust'])  # Write header to CSV file
    
    # This function is called periodically from FuncAnimation
    def animate(i):
        global xs, ys, rs
        
        # Acquire data from serial port
        line = ser.readline().decode().strip()  # Convert bytes to string and remove whitespace
        if not line:
            return line_exp, line_theo  # Return empty lines if no data
        
        print("Received:", line)  # Print received data for debugging
        
        # Extract time and thrust values
        try:
            time_val, thrust_val = map(int, line.split("|"))
        except ValueError:
            print("Parsing error:", line)  # Print parsing error for debugging
            return line_exp, line_theo  # Return empty lines if data cannot be parsed
        
        # Write data to CSV file
        csvwriter.writerow([time_val, thrust_val])
        
        # Update data lists
        xs.append(time_val)
        ys.append(thrust_val)
        rs.append(0.5)

        # Update plot data
        line_exp.set_data(xs, ys)
        line_theo.set_data(xs, rs)
        
        # Adjust plot limits
        ax.set_xlim(min(xs), max(xs))  # Set x-axis limits dynamically
        ax.set_ylim(min(0, min(ys)), max(1200, max(ys)))  # Set y-axis limits dynamically

        return line_exp, line_theo  # Return the artists to be updated

    # Set up plot to call animate() function periodically
    ani = animation.FuncAnimation(fig, animate, interval=100, blit=True)

    # Show the plot
    plt.show()
