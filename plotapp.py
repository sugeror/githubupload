import json

from flask import Flask,render_template,request
import pandas as pd
import json
import plotly
import plotly.express as px
import MySQLdb

db=MySQLdb.connect(host='localhost',user='root',password='1234',db='tbl_plot')
cur = db.cursor()

# sql = "insert into tbl_plot(name,age, values(%s, %s, %s, %s, %s, %s)"

app =Flask(__name__)

@app.route('/')
def bar_with_plotly():
    # Students data available in a list of list
    # students = [['Akash', 34, '시드니', '오스트레일리아'],
    #             ['Rithika', 30, 'Coimbatore', '인디아'],
    #             ['Priya', 31, 'Coimbatore', '인디아'],
    #             ['Sandy', 32, '도쿄', '재팬'],
    #             ['Praneeth', 16, '뉴욕', '유에스'],
    #             ['Praveen', 17, '토론토', '캐나다']]
    sql = "select * from tbl_plot";
    cur.execute(sql)
    datas = cur.fetchall();
    for i in datas:
        print(i);
    df =pd.DataFrame(datas, columns=['no','Name','Age','City','Country'],index=['a','b','c','d','e','f','g'])
    # #Bar chart 생성
    fig = px.bar(df,x='Name',y='Age',color='City',barmode='group')
    #
    # #graphjson 생성
    graphJson = json.dumps(fig, cls=plotly.utils.PlotlyJSONEncoder)
    #
    return render_template('bar.html',graphJson=graphJson)
if __name__=='__main__':
    app.run(debug=True)

