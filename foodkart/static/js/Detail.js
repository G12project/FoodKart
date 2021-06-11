var counter = 1;

function increment() {
	if (counter >= 0) {
		counter++;
		document.getElementById("xyz").href = "/addcart/{{object.id}}/" + counter;
		document.getElementById("max").value = counter;
	}
}
function decrement() {
	if (counter >= 1) {
		counter--;
		document.getElementById("xyz").href = "/addcart/{{object.id}}/" + counter;
		document.getElementById("max").value = counter;
	}
}