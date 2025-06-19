# AI-On-Web
A website made with pythons flask library and the ollama libary.

# How to install:
`pip install -r requirments.txt`
or just do
`pip install flask ollama`

Put the main.py file and the template in one folder, run main.py and find the ip it gives you, usually `127.0.0.1:5000`

# What if im already using that port?
If you are already using port 5000 (default port for flask) then you can change the port by adding `port=` then the port needed at the last line `app.run(debug=True, port=----)`

Full Example:
`if __name__ == "__main__":
    app.run(debug=True, port=5003)`
(The port can be any unused port)
