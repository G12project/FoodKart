
function geoFindMe() {

		function showPosition(position){
			mapboxgl.accessToken = 'pk.eyJ1IjoieWFzaDQ1NTYiLCJhIjoiY2tvaG9hbXdnMTFpYzJub2MxOXJ5emxyNyJ9.EWWBTTl5gYAZ_HRXhoSEew';
			var map = new mapboxgl.Map({
					container: 'map', // Container ID
				style: 'mapbox://styles/mapbox/streets-v11', // Map style to use
				center: [position.coords.longitude, position.coords.latitude], // Starting position [lng, lat]
				zoom: 12 // Starting zoom level
			});

			var marker = new mapboxgl.Marker() // Initialize a new marker
				.setLngLat([position.coords.longitude, position.coords.latitude]) // Marker [lng, lat] coordinates
				.addTo(map);
		}
		// const status = document.querySelector('#status');
		// const mapLink = document.querySelector('#map-link');

		// mapLink.href = '';
		// mapLink.textContent = '';
		function success(position) {
			document.my_form.Latitude.value = position.coords.latitude;
			document.my_form.Longitude.value = position.coords.longitude;
			showPosition(position)
			// status.textContent = '';
			// mapLink.href = `https://www.openstreetmap.org/#map=18/${latitude}/${longitude}`;
			// mapLink.textContent = `Latitude: ${latitude} °, Longitude: ${longitude} °`;
		}

		function error() {
			status.textContent = 'Unable to retrieve your location';
		}

		if (!navigator.geolocation) {
			status.textContent = 'Geolocation is not supported by your browser';
		} else {
			status.textContent = 'Locating…';
			navigator.geolocation.getCurrentPosition(success, error);
		}

	}
document.querySelector('#locate').addEventListener('click', geoFindMe);