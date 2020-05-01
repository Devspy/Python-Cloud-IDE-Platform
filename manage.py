import os
import subprocess




print("Welcome To Setup python Cloud IDE")
print("\nNote: you need to Install Docker-ce First Then Continue")
print("1.To Download Docker Image (If already present then skip)")
print("2.Configure ClOUD IDE")
print("3.Start IDE Service")
print("4.Stop IDE Service")
print("5.Remove Container in Server")

st=subprocess.getoutput("systemctl restart docker")
ch=int(input("Enter your choice:"))

if(ch==1):
	print("please wait your Downloading take several minutes")
	x1=subprocess.getoutput("docker pull theiaide/theia-python")
	print(x1)
	print("Download Sucessfully")
elif(ch==2):
	y=subprocess.getoutput("pip install docker-compose")
	print(y)
	print("Sucessfully installed Docker-compose")
	f=open('docker-compose.yml','w')
	f.write("""version: '3'

services:
  IDE:
    image: theiaide/theia-python
    volumes:
      - myworkbench:/home/project
    restart: always
    ports:
      - 555:3000

volumes:
  myworkbench:""")
	f.close()
	x2=subprocess.getoutput("chmod +x docker-compose.yml")
	x3=subprocess.getoutput("docker-compose up -d")
	print("Sucessfully Configure your cloud IDE")
	print("Default port number is 555")
	print("check Server IP and use, For eg:(192.168.43.6:555) use in Browser for access IDE")

elif(ch==3):
	x3=subprocess.getoutput("docker-compose start")
	print("Service Started")
elif(ch==4):
	x4=subprocess.getoutput("docker-compose stop")
	print("service stoped")
elif(ch==5):
	x5=subprocess.getoutput("docker-compose stop")
	x6=subprocess.getoutput("docker-compose rm -f")
	print("Container Sucessfully Removed")

else:
	print("Wrong Input")
        


