import math
class project1:
 
 g=10 #gravitational constant
 r=6371 #approximate radius of earth
 dist=0

 def Haversine(self,latp,lat_target,lonp,lon_target): #calculating distance between two points using haversine formula
     
    latp = (latp) * math.pi / 180.0 #converting all coordinates in degrees to radians
    lat_target = (lat_target) * math.pi / 180.0
    lonp = (lonp) * math.pi / 180.0
    lon_target = (lon_target) * math.pi / 180.0

    a=pow(math.sin((lat_target-latp)/2),2)
    b=math.cos(lat_target)*math.cos(latp)*pow(math.sin((lon_target-lonp)/2),2)
    self.dist=2*self.r*math.asin(math.sqrt(a+b))#in kilometers
    theta=self.dist/self.r

    print(self.dist)#distance in kilometers
    print(theta)#central angle in radians
 '''def Trajectory(self,theta,vel_x,dist):

   print(math.sin(theta/2))
   b=(2*self.r*self.g*math.sin(theta/2))/(pow(vel_x,2))
   theta_dash=0.5*math.asin(b)
   print (theta_dash)
   for i in range(0,dist,+10):
    x=i
    if(theta_dash<math.pi//2):
     y=x*math.tan(theta_dash)-self.g*pow(x,2)/(2*pow(vel_x,2)*pow(math.cos(theta_dash),2))
     print(y)'''
 def Trajectory(self,vel_x,total_weight,payload):
   H=20
   u=vel_x
   D=math.sqrt(2*u*u*H/self.g)#horizontal range of the payload
   dist_travel=self.dist-D
   print(D)
   '''for i in range(1,math.floor(D),+5):#generates a parabolic trajectory
     x=i
     y=self.g*x*x/(2*u*u)
     print(y)'''
   for i in range(0,math.floor(self.dist)):
     if(i==math.floor(dist_travel)):
       print("payload is dropped at",dist_travel)
       total_weight=total_weight-payload
       vel_x=0# drone must stop
 def Drag(self,density,area,drag_coeff,drag_force,wind_vel):
   v1=math.sqrt(2*drag_force/(density*drag_coeff*area))
   v=v1+wind_vel #velocity of uav wrt ground=velocity of uav wrt medium+ velocity of medium wrt ground
   print(v)  


get=project1()
get.Haversine(50.066389,53.643889,-5.711944,-3.070000)
get.Trajectory(5,60,1.5)

