<html>
<body>
<h1>Word Counter Application</h1>
<a href="{% url 'about'%}"><input type="button" value="About" /></a>
<form action="{% url 'count' %}">
<textarea id="inputBox" name="inputBox" rows="10" cols="40" style="resize: none;"></textarea>
<div>
<input type="submit" value="Count" />
</div>
</form>
</body>
</html>
