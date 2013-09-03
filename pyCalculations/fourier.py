# Function for taking 1d and 2d fourier transforms here.

def fourier( t, y, kaiserwindowparameter=0 ):
   ''' Function for returning fourier series and frequencies of some given arrays t and y
       NOTE: t must have a constant time stepping
       :param t            The time variable
       :param y            Some variable data
       :returns the frequencies, new time variables and frequencies
       return format: [frequencies, t, y]

       Example usage:
       fourier_data = fourier( t=np.arange(0,500,0.5), y=rho_data, kaiserwindowparameter=14 )
   '''
   # Get the data
   from variable import get_data
   t_data = get_data(t)
   y_data = get_data(y)
   # First check the t array whether it has a constant dt
   dt = t_data[1] - t_data[0]
   for i in xrange(len(t_data)-1):
      if dt != t_data[i+1] - t_data[i]:
         print "Gave bad timestep to plot_fourier, the time step in array t must be constant (for now)"
   # Use kaiser window on y
   y_data = y_data*np.kaiser(len(y_data), kaiserwindowparameter)
   # Do FFT on the data
   fourier=np.fft.fft(y_data)*(1/(float)(len(t_data)))
   # Get frequencies of the fourier
   freq=np.fft.fftfreq(len(fourier), d=dt)
   # Declare t2 (Note: This is the same as t but we want the steps to be thicker so the data looks smoother
   dt2=dt*0.01
   t2=np.arange(len(t_data)*100)*dt2
   # Declare y2
   y2=np.array([np.sum(fourier*np.exp(complex(0,1)*2*np.pi*freq*T)) for T in t2])
   from output import output_1d
   from variable import get_name
   return output_1d([freq, t2, y2], ["frequency", "time", get_name(y)])

