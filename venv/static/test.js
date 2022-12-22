console.log("true!")
function submt(){
	btm = document.getElementById("myform");
	//btm.submit();
	f = new FormData(btm);
	fetch("http://127.0.0.1:5000/ping", {body: f, method: "post"});
	
	btm.reset();
}