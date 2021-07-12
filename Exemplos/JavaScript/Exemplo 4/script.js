function somar(){
	var num1 = document.getElementById("num1").value;
	var num2 = document.getElementById("num2").value;
	var soma = parseFloat(num1) + parseFloat(num2);
	var resultado = document.getElementById("resultado");
	resultado.innerText = soma;
}