$(function() {
	'use strict';
	var locationLat = 0;
	var locationLong = 0;
    var zoomLevel = parseInt("13");

	$(".container").hide();
	getLocation();

    $("#default").click(function() {
        zoomLevel = parseInt("13");
        $("#level").val("1.5");
        createMap();    
    });

    $("#level").change(function() {
        if ($("#level").val() == "1.5") {
            zoomLevel = parseInt("13");
        }
        createMap();
    });

//	$(window).resize(function() {
//		var mapHeight = window.innerHeight * 0.5;
//		var mapWidth = window.innerHeight * 0.6;
//		document.getElementById("map").innerHTML = "";
//		createMap();
//	});
});

function getLocation() {
    if (navigator.geolocation) {
        navigator.geolocation.getCurrentPosition(setPosition, showError);
    } else {
        alert("Geolocation is not supported.");
    }
}

function setPosition(position) {
	$("#error").toggle();
	$(".container").fadeToggle();			
	locationLat = position.coords.latitude;
	locationLong = position.coords.longitude;
	createMap();
}

function createMap() {
    $("#map").empty();
	var map = new Microsoft.Maps.Map(document.getElementById('map'), {credentials: 'AgnpgjJOhsPeO0tYd2JJZMYnwtIKjPnjkZuGOfPHIMZeEGbDxRq-ZLgAnl98icuL', 
	center: new Microsoft.Maps.Location(locationLat, locationLong), zoom: 13, disableZooming: true, showDashboard: false, enableSearchLogo: false, width: 500, height: 500});
    
    map.entities.clear(); 
    var pushpinOptions = {icon: 'http://ddragon.leagueoflegends.com/cdn/5.20.1/img/profileicon/937.png', width: 70, height: 70}; 
    var pushpin= new Microsoft.Maps.Pushpin(map.getCenter(), pushpinOptions);
    map.entities.push(pushpin);
}

function showError(error) {
	document.getElementsByClassName("container")[0].innerHTML = "<h1>Please enable location services.</h1>";
    switch(error.code) {
        case error.PERMISSION_DENIED:
            console.log("User denied the request for Geolocation.");
            break;
        case error.POSITION_UNAVAILABLE:
        	console.log("Location information is unavailable.");
            break;
        case error.TIMEOUT:
        	console.log("The request to get user location timed out.");
            break;
        case error.UNKNOWN_ERROR:
        	console.log("An unknown error occurred.");
            break;
    }
}