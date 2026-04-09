Monto Carlo Pi Simulation

Description: Approximate pi using random sampling inside a 1x1 square

Method:
- Generate (x,y) points
- Count how many points are inside the unit circle
- pi ~= 4 * inside / total points

Results:
- Error decreases by roughly sqrt(1/n)
Monte Carlo estimation of pi using 200,000 samples.
![Pi Simulation](pi_plot.png)

Features:
- Batch processing for performance
- Visualization of points inside and outside of the unit circle