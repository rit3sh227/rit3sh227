import time
import matplotlib.pyplot as plt
from pytube import Channel

# Replace 'CHANNEL_URL' with the URL of the YouTube channel you want to track.
CHANNEL_URL = 'https://www.youtube.com/c/YOUR_CHANNEL_NAME'

# Initialize the YouTube channel object
channel = Channel(CHANNEL_URL)

# Initialize data lists to store timestamps and subscriber counts
timestamps = []
subscriber_counts = []

def get_subscriber_count():
    """Fetches the current subscriber count of the channel."""
    channel.subscribe()
    return channel.subscriber_count

def plot_subscriber_count():
    """Plots the subscriber count over time."""
    plt.figure(figsize=(10, 6))
    plt.plot(timestamps, subscriber_counts, color="blue", marker="o")
    plt.title("YouTube Subscriber Count Over Time")
    plt.xlabel("Time")
    plt.ylabel("Subscriber Count")
    plt.grid()
    plt.show()

try:
    # Start tracking
    while True:
        # Get current time and subscriber count
        current_time = time.strftime("%H:%M:%S")
        subscriber_count = get_subscriber_count()

        # Append data to lists
        timestamps.append(current_time)
        subscriber_counts.append(subscriber_count)

        # Print the current count (for logging purposes)
        print(f"{current_time} - Subscribers: {subscriber_count}")

        # Update the plot
        plt.clf()  # Clear previous plot
        plt.plot(timestamps, subscriber_counts, color="blue", marker="o")
        plt.title("YouTube Subscriber Count Over Time")
        plt.xlabel("Time")
        plt.ylabel("Subscriber Count")
        plt.xticks(rotation=45)
        plt.tight_layout()
        plt.pause(60)  # Update plot every 60 seconds

        # Sleep for a minute before getting the next count
        time.sleep(60)

except KeyboardInterrupt:
    print("Tracking stopped.")
    plot_subscriber_count()  # Final plot when tracking stops
