function geoFindMe() {
	// const status = document.querySelector('#status');
	// const mapLink = document.querySelector('#map-link');

	// mapLink.href = '';
	// mapLink.textContent = '';
	function success(position) {
		var latitude = position.coords.latitude;
		var longitude = position.coords.longitude;
		var firebaseConfig = {
			apiKey: "AIzaSyDfGQmsSdjAM77R7g4rkCa_d7FXsaPcl_I",
			authDomain: "test2-374dc.firebaseapp.com",
			databaseURL: "https://test2-374dc-default-rtdb.asia-southeast1.firebasedatabase.app",
			projectId: "test2-374dc",
			storageBucket: "test2-374dc.appspot.com",
			messagingSenderId: "900145299510",
			appId: "1:900145299510:web:baed02e2b01bd767225897"
		};
		firebase.initializeApp(firebaseConfig);
		var user_id = JSON.parse(document.getElementById('user_id').textContent);
		// firebase.analytics();
		firebase.database().ref('DeliveryExec/' + parseInt(user_id)).set({
			currlat: latitude,
			currlong: longitude,
			is_busy: false
		}).then((error) => {
			if (error) {
				console.log("Error");
			}
			else {
				window.location.href = "/delhome";
			}

		});
		var showCurrentData = firebase.database().ref('DeliveryExec');
		showCurrentData.on('value', (snapshot) => {
			const data = snapshot.val();
			console.log(data);
		});
		// Move to a new location or you can do something else
		// Redirect();

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