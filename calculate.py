import cgi
import datetime

print("Content-type: text/html\n")

form = cgi.FieldStorage()
a = float(form.getvalue("a", 1))
b = float(form.getvalue("b", 1))
c = float(form.getvalue("c", 1))

c_cubed = c ** 3
sqrt_c_cubed = c_cubed ** 0.5
division = sqrt_c_cubed / a
multiplied = division * 10
final_result = multiplied + b
timestamp = datetime.datetime.now()

print(f"""
<html>
<head><title>Assignment #2</title></head>
<body>
<h1>Assignment #2</h1>
<p>Final Result: {final_result}</p>
<p>Step 1: c = {c}, c³ = {c_cubed}</p>
<p>Step 2: √(c³) = {sqrt_c_cubed}</p>
<p>Step 3: {sqrt_c_cubed} / {a} = {division}</p>
<p>Step 4: {division} * 10 = {multiplied}</p>
<p>Step 5: {multiplied} + {b} = {final_result}</p>
<p>Calculation completed at {timestamp.strftime('%Y-%m-%d %H:%M:%S')}</p>
</body>
</html>
""")