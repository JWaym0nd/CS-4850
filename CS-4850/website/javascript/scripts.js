function showLocation()
{
	if(document.getElementById("location").style.display == "none")
		document.getElementById("location").style.display = "block";
	else
		document.getElementById("location").style.display = "none";
}
function showRestaurant()
{
	if(document.getElementById("restaurant").style.display == "none")
		document.getElementById("restaurant").style.display = "block";
	else
		document.getElementById("restaurant").style.display = "none";
}
function showOrder()
{
	if(document.getElementById("order").style.display == "none")
		document.getElementById("order").style.display = "block";
	else
		document.getElementById("order").style.display = "none";
}

var x = document.getElementById("latlong");
function getLocation() {
	var zipcode = document.getElementById('zipcode').value;

	if(zipcode == "")
	{
		document.getElementById("zipcode").focus();
		document.getElementById("zipcodeerror").innerHTML = "Please Enter Your Zip Code";
	}
	else
	{
		document.getElementById("zipcodeerror").innerHTML = "";
		if (navigator.geolocation) {
			navigator.geolocation.getCurrentPosition(showPosition);
		  } else {
			x.innerHTML = "Geolocation is not supported by this browser.";
		  }
	}
}
function showPosition(position) {
  x.innerHTML = "Latitude: " + position.coords.latitude +
  "<br>Longitude: " + position.coords.longitude;
}
