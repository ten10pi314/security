import java.io.*;
import java.lang.*;
import java.net.*;

public class honeypot {

	private static ServerSocket server;
	private static int port = 22;

	public static void main(String args[]) throws Exception{
    	server = new ServerSocket(port);
    	System.out.println("Honeypot running on port:" + port);
    	Socket socket = server.accept();
    	System.out.println("Incoming connection:");
    	System.out.println("IP:" + socket.getInetAddress());
    	System.out.println("Port:" + socket.getPort());
    	System.out.println("local port:" + socket.getLocalPort());
    	socket.close();
    	System.out.println("Shutting down Honeypot");
    	server.close();
	}
}
/*
Terminal 1:
$ sudo service ssh stop
$ javac honeypot.java
$ sudo java honeypot
Honeypot running on port:22
Incoming connection:
IP:/127.0.0.1
Port:51144
local port:22
Shutting down Honeypot

Terminal 2:
$ ssh localhost
ssh_exchange_identification: Connection closed by remote host
*/
