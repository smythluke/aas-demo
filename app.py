from flask import Flask, redirect, request, Markup
app = Flask(__name__)

posts = []

@app.route("/")
def index():
   # Render the main page
   output = """
      <form action='sendmsg' method='post'>
         <input type='text' name='msg'>
         <input type='submit' value='Submit'>
      </form>
      <form action='refresh'>
         <input type='submit' value='Refresh'>
      </form>
      <h1>POSTS:</h1>
   """
   for post in posts:
      output += "<p>" + post + "</p>"
   return output

@app.route("/sendmsg", methods=["POST"])
def post():
   # Add message to the list of posts and go back to the main page
   # Fix 3: Escape user-supplied input to make it safe
   posts.append(str(Markup.escape(request.form["msg"])))
   return redirect("/")

@app.route("/refresh")
def refresh():
   # Fix 2: No user-supplied URL redirection
   return redirect("/")

if __name__ == "__main__":
   # Fix 1: no debug in production!
   app.run(debug=False)
