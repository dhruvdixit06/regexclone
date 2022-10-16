from flask import Flask, render_template,request
import re

backend=Flask(__name__)

@backend.route('/',methods=['POST','GET'])
def match():
    if request.method=='POST':
        n=request.form['regex']
        s=request.form['string']
        c=0
        res=[]
        for it in re.finditer(r"{}".format(n),s):
            st=""
            c=c+1
            st=st+"Match {} \"{}\" at start index: {} and end index: {}".format(c,it.group(),it.start(),it.end())
            res.append(st)
        return render_template("frontend.html",ans="Match Found!",regex=n,string=s,count=c,spans=res)
    return render_template("frontend.html",count=-1)

if __name__=='__main__':
    backend.run(debug=True)
