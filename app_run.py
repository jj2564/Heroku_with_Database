from flask import *
from datetime import datetime
from dbModel import *

@app.route('/')
@app.route('/index')
def index():
    data = "群組小幫手"
    data_UserData = UserData.query.all()
    userdata_dic = {}
    userdata_list = []
    for _data in data_UserData:
        userdata_dic['id'] = _data.id
        userdata_dic['display_name'] = _data.display_name
        userdata_dic['status_message'] = _data.status_message
        userdata_dic['create_date'] = _data.create_date.strftime('%Y/%m/%d %H:%M:%S')
        userdata_list.append(userdata_dic)
    return render_template('index.html', **locals())

@app.route('/API/insert_data', methods=['POST'])
def insert_data():
    name = request.form['display_name']
    message = request.form['status_message']
    if name != "" and message != "":
        insert_data = UserData(
        	user_id=123,
            display_name=name,
            picture_url='unknown',
            status_message=message,
            group_id=321,
            create_date=datetime.now(),
            modify_date=datetime.now()
        )
        db.session.add(insert_data)
        db.session.commit()
        #loadUserData()
    return redirect('index')


if __name__ == '__main__':
    app.run(debug=True)
