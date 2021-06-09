
function success(position) {
    const latitude = position.coords.latitude;
    const longitude = position.coords.longitude;
    console.log(latitude + " " + longitude);
    var firebaseConfig = {
        apiKey: "AIzaSyDfGQmsSdjAM77R7g4rkCa_d7FXsaPcl_I",
        authDomain: "test2-374dc.firebaseapp.com",
        databaseURL: "https://test2-374dc-default-rtdb.asia-southeast1.firebasedatabase.app",
        projectId: "test2-374dc",
        storageBucket: "test2-374dc.appspot.com",
        messagingSenderId: "900145299510",
        appId: "1:900145299510:web:baed02e2b01bd767225897"
    };
    if (!firebase.apps.length) {
        firebase.initializeApp(firebaseConfig);
    } else {
        firebase.app(); // if already initialized, use that one
    }
    var user_id = JSON.parse(document.getElementById('user_id').textContent);
    var ref = firebase.database().ref('DeliveryExec/' + "{{user_id}}");
    ref.update({
        currlat: latitude
    });
    ref.update({
        currlong: longitude
    });
    ref.update({
        is_busy: true
    });
    var showCurrentData = firebase.database().ref('DeliveryExec');
    showCurrentData.on('value', (snapshot) => {
        const data = snapshot.val();
        console.log(data);
    });
}

function error() {
    alert('Sorry, no position available.');
}

const options = {
    enableHighAccuracy: true,
    maximumAge: 30000,
    timeout: 27000
};

const watchID = navigator.geolocation.watchPosition(success, error, options);

        var firebaseConfig = {
        apiKey: "AIzaSyDfGQmsSdjAM77R7g4rkCa_d7FXsaPcl_I",
        authDomain: "test2-374dc.firebaseapp.com",
        databaseURL: "https://test2-374dc-default-rtdb.asia-southeast1.firebasedatabase.app",
        projectId: "test2-374dc",
        storageBucket: "test2-374dc.appspot.com",
        messagingSenderId: "900145299510",
        appId: "1:900145299510:web:baed02e2b01bd767225897"
    };
    if (!firebase.apps.length) {
        firebase.initializeApp(firebaseConfig);
    } else {
        firebase.app(); // if already initialized, use that one
    }
    var ref = firebase.database().ref('Orders/' + "{{orderid}}");
    ref.update({
        del_id: parseInt("{{user_id}}")
    });
    var showCurrentData = firebase.database().ref('Orders');
    showCurrentData.on('value', (snapshot) => {
        const data = snapshot.val();
        console.log(data);
    });
    function PickupOrder() {
            ref.update({
            curr_status: 4
        });
    }
    function Delivered(){
        ref.update({
            curr_status: 5
        });
    }
