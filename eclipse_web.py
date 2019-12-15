import matplotlib.pyplot as plt
import numpy as np
import urllib

url    = 'http://skywatch.colorado.edu/data/spn/spn_17_08_21.dat'
lines  = urllib.request.urlopen(url).readlines()

# Loop over the lines in the file
utc=[] # initialize list for times
tti=[] # initialize list for total irradiance
ttd=[] # initialize list for diffuse irradiance
for line in lines:
    entries = line.decode("utf-8").split(",")
    #print(entries);quit()
    if entries[0][0] != ';':
        utc.append(float(entries[0][0:2]) + \
                   float(entries[0][3:5])/60. + \
                   float(entries[0][6:8])/3600.)
        tti.append(float(entries[1]))      
        ttd.append(float(entries[2]))

# Append +24 hours if data was measured on next day
utc=np.array(utc)
next_day=np.where(utc < 7) # This is not quite clean, cut off at locat midnight
utc[next_day]=utc[next_day]+24.

# Now do the plotting
plt.close() # closes previous plot
fig=plt.figure(figsize=[6,6]) 
plt.plot(utc,tti,'o',markersize=1,label='Total') 
plt.plot(utc,ttd,'or',markersize=1,label='Diffuse')
plt.xlabel('UTC [h]',fontsize=14)
plt.ylabel('Irradiance [W m$^{-2}$]',fontsize=14) 
plt.title('Solar Eclipse',fontsize=18)
plt.legend(fontsize=14)
plt.show()
fig.savefig('eclipse.png',dpi=600)




