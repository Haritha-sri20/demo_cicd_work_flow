from flask import Flask, make_response

app = Flask(__name__)

@app.route('/')
def hello_world():
    # HTML content with a specific text color
    html_content = ''' <marquee direction="left" behavior="scroll" scrollamount="5" style="color: blue; font-size: x-large;">
    Hello, Welcome to my Webpage, Team DevOps SOFTILITY </marquee>
    <br>
    <marquee direction="left" behavior="scroll" scrollamount="5" style="color: green; font-size: x-large;">
        Good news guys
    </marquee>
    <img src="softility_inc_cover.jfif" alt="Sample Image" width="500" height="300">'''
    
    response = make_response(html_content)
    
    # Adding minimum required headers
    response.headers['Content-Type'] = 'text/html; charset=utf-8'
    response.headers['Server'] = 'Flask'
    
    return response

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=9090)
