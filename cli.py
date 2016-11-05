#!/usr/bin/env python
import os
from flask import Flask, render_template,request,redirect,url_for,send_from_directory
import sys
application = Flask(__name__)

HOST = "ec2-....compute.amazonaws.com"


@application.route('/',methods=['GET'])
def run():
    return render_template("index.html")

@application.route('/command',methods=['GET'])
def command():
    cmd1= "sudo chmod +x /home/ubuntu/mapper.py"
    cmd2= "sudo chmod +x /home/ubuntu/reducer.py"
    cmd3= "hadoop fs -mkdir -p /input"
    cmd4= "hadoop fs -put /home/ubuntu/input_file.csv /input/input_file.csv"
    cmd5= "hadoop jar /usr/local/hadoop/share/hadoop/tools/lib/hadoop-streaming-2.7.1.jar -file /home/ubuntu/mapper.py -mapper 'mapper.py' -file /home/ubuntu/reducer.py -reducer 'reducer.py' -input /input_file.csv -output /output > abc.txt"
    os.system (cmd1)
    return. render_template ("output.html")



if __name__=="__main__":
    app.run()