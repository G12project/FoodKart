
		// Your web app's Firebase configuration
		// For Firebase JS SDK v7.20.0 and later, measurementId is optional
  var firebaseConfig = {
    apiKey: "AIzaSyBx5xyBnj2YjJQJhUlwR1kLaREMxgEfT3M",
    authDomain: "foodkart-7de2e.firebaseapp.com",
    databaseURL: "https://foodkart-7de2e-default-rtdb.asia-southeast1.firebasedatabase.app",
    projectId: "foodkart-7de2e",
    storageBucket: "foodkart-7de2e.appspot.com",
    messagingSenderId: "787811737622",
    appId: "1:787811737622:web:ac4fd20d534149b0ec1537",
    measurementId: "G-XGD6E0YRM4"
  };
  // Initialize Firebase
  firebase.initializeApp(firebaseConfig);
  firebase.analytics();
function writeOrder(rest_id, rest_name, item_list,pickuplat, pickuplong, cust_id, cust_name, del_lat, del_long, del_id){
	itempricelist={};
	item_list.array.forEach(item => {
		itempricelist[item[0]]=item[1];
	});
	console.log(itempricelist);
	firebase.database().ref('Orders/').set({
		rest_id: rest_id,
		rest_name: rest_name,
		items: itempricelist,
		pickuplat: pickuplat,
		pickuplong: pickuplong,
		cust_id: cust_id,
		cust_name: cust_name,
		del_lat: del_lat,
		del_long: del_long,
		del_id: del_id
	});
	var showCurrentData = firebase.database().ref('student');
	showCurrentData.on('value', (snapshot) => {
		const data = snapshot.val();
		console.log(data);
	});
}