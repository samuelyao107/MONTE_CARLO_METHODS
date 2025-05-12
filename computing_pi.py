import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation
from matplotlib.patches import Circle, Rectangle
import math


n_points_per_frame = 100
max_points = 10000


fig = plt.figure(figsize=(14, 8))
grid = plt.GridSpec(2, 3, height_ratios=[3, 1], width_ratios=[1, 1, 1], hspace=0.3, wspace=0.15)


ax1 = plt.subplot(grid[0, :2])
ax1.set_xlim(-1.05, 1.05)
ax1.set_ylim(-1.05, 1.05)
ax1.set_aspect('equal')
ax1.grid(alpha=0.3)
ax1.set_title("Monte Carlo Approximation of π", fontsize=14)


ax2 = plt.subplot(grid[0, 2])
ax2.set_title("π Approximation Evolution", fontsize=14)
ax2.set_xlabel("Number of Points")
ax2.set_ylabel("π Approximation")
ax2.grid(alpha=0.4)
ax2.axhline(y=math.pi, color='blue', linestyle='--', alpha=0.7, label=f'True π = {math.pi:.6f}')
ax2.legend(loc='upper right')


ax_stats = plt.subplot(grid[1, :])
ax_stats.axis('off')


circle = Circle((0, 0), 1, fill=False, color='blue', linewidth=2)
square = Rectangle((-1, -1), 2, 2, fill=False, color='black', linewidth=2)
ax1.add_patch(circle)
ax1.add_patch(square)


stats_text = ax_stats.text(0.01, 0.6, "", fontsize=12, ha='left', va='top')


points_inside_x, points_inside_y = [], []
points_outside_x, points_outside_y = [], []
pi_values = []
point_counts = []


inside_scatter = ax1.scatter([], [], s=5, color='green', alpha=0.6)
outside_scatter = ax1.scatter([], [], s=5, color='red', alpha=0.6)

pi_line, = ax2.plot([], [], 'r-', lw=2)

def init():
    """Initialize the animation"""
    inside_scatter.set_offsets(np.empty((0, 2)))
    outside_scatter.set_offsets(np.empty((0, 2)))
    pi_line.set_data([], [])
    stats_text.set_text("")
    return inside_scatter, outside_scatter, pi_line, stats_text

def update(frame):
    """Update the animation for each frame"""
    global points_inside_x, points_inside_y, points_outside_x, points_outside_y, pi_values, point_counts
    
    
    for _ in range(n_points_per_frame):
        x, y = np.random.uniform(-1, 1, 2)
        if x**2 + y**2 <= 1:
            points_inside_x.append(x)
            points_inside_y.append(y)
        else:
            points_outside_x.append(x)
            points_outside_y.append(y)
    
   
    inside_scatter.set_offsets(np.column_stack((points_inside_x, points_inside_y)))
    outside_scatter.set_offsets(np.column_stack((points_outside_x, points_outside_y)))
    
    
    total_points = len(points_inside_x) + len(points_outside_x)
    if total_points > 0:
        pi_approx = 4 * len(points_inside_x) / total_points
        pi_error = abs(pi_approx - math.pi)
        pi_accuracy = (1 - pi_error/math.pi) * 100
        
        
        pi_values.append(pi_approx)
        point_counts.append(total_points)
        
        
        pi_line.set_data(point_counts, pi_values)
        ax2.set_xlim(0, max(point_counts) * 1.1)
        
        
        max_error = max(0.1, max([abs(pv - math.pi) for pv in pi_values]))
        ax2.set_ylim(math.pi - max_error*1.5, math.pi + max_error*1.5)
        
        
        stats = f"""
Points inside circle: {len(points_inside_x):,} ({len(points_inside_x)/total_points*100:.2f}%)
Points outside circle: {len(points_outside_x):,} ({len(points_outside_x)/total_points*100:.2f}%)
Total points: {total_points:,}
π approximation: {pi_approx:.8f}
True π value: {math.pi:.8f}
Error: {pi_error:.8f} ({pi_accuracy:.4f}% accurate)
        """
        stats_text.set_text(stats)
    
    
    if total_points >= max_points:
        ani.event_source.stop()
        
    return inside_scatter, outside_scatter, pi_line, stats_text


ani = animation.FuncAnimation(
    fig, update, frames=range(max_points//n_points_per_frame),
    init_func=init, blit=True, interval=50)

plt.tight_layout()


plt.show()
