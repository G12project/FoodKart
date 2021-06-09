var firebaseConfig = {
  apiKey: "AIzaSyDfGQmsSdjAM77R7g4rkCa_d7FXsaPcl_I",
  authDomain: "test2-374dc.firebaseapp.com",
  databaseURL: "https://test2-374dc-default-rtdb.asia-southeast1.firebasedatabase.app",
  projectId: "test2-374dc",
  storageBucket: "test2-374dc.appspot.com",
  messagingSenderId: "900145299510",
  appId: "1:900145299510:web:baed02e2b01bd767225897"
};
var orderid = JSON.parse(document.getElementById('orderid').textContent);
var url = '/restordercheck/' + orderid;
firebase.initializeApp(firebaseConfig);
var db = firebase.database();
// var orderid = JSON.parse(document.getElementById('orderid').textContent);
var events = db.ref('Orders/' + orderid);
var query = db.ref('Orders/');
query.child(orderid).get().then((snapshot) => {
  if (snapshot.exists()) {
    console.log(snapshot.val())
      ; document.getElementById('cust_name').innerHTML = snapshot.val().cust_name;
    var lat = snapshot.val().del_lat;
    var long = snapshot.val().del_long;
    const url = "https://api.mapbox.com/geocoding/v5/mapbox.places/" + long + "," + lat + ".json?access_token=pk.eyJ1IjoieWFzaDQ1NTYiLCJhIjoiY2tvaG9hbXdnMTFpYzJub2MxOXJ5emxyNyJ9.EWWBTTl5gYAZ_HRXhoSEew";
    $.getJSON(url, function (ans) {
      $('#address').html(ans.features[0].place_name);
    });
    var content = '';
    for (k in snapshot.val().item_list) {
      content += '<tr>';
      content += '<td>' + k + '</td>';
      content += '<td>' + snapshot.val().item_list[k]['quantity'] + '</td>';
      var x = snapshot.val().item_list[k]['quantity'] * snapshot.val().item_list[k]['price']
      content += '<td>' + x + '</td>';
    }
    var arr = [];
    arr[0] = 'Waiting'; arr[1] = 'Confirmed'; arr[2] = 'Preparing'; arr[3] = 'Waiting for Delivery'; arr[4] = 'Out for Delivery'; arr[5] = 'Delivered';
    document.getElementById('curr_status').innerHTML = arr[snapshot.val().curr_status];
    $('#ex-table').html(content);
  }
});
function OkOrder() {
  console.log(orderid);
  events.update({
    curr_status: 1
  });
  window.location.href = url;
}
function prepareOrder() {
  // var orderid = JSON.parse(document.getElementById('orderid').textContent);
  events.update({
    curr_status: 2
  });
  window.location.href = url;
}
function requestdel() {
  // var orderid = JSON.parse(document.getElementById('orderid').textContent);
  events.update({
    curr_status: 3
  });
  window.location.href = url;
}