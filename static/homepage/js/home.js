$(document).ready(function () {
    function addcart(id) {
	num = $("#num").val();
	$.post('/product/addtocart', {
		'id': id,
		'num': num,
		'csrfmiddlewaretoken': '{{csrf_token}}'
	}, function (data) {
		alert('add success');
	});
}
});

function addcart(id) {
	num = $("#num").val();
	$.post('/product/addtocart', {
		'id': id,
		'num': num,
		'csrfmiddlewaretoken': '{{csrf_token}}'
	}, function (data) {
		alert('add success');
	});
}



function deletecart(id) {
	$.post('/product/deletecart', {
		'id': id,
		'csrfmiddlewaretoken': '{{csrf_token}}'
	}, function (data) {
		alert('delete success');
		location.reload();
	});
}

$(function () {
	$(".update-cart").change(function () {
		let $this = $(this);
		let id = $this.attr('data-id')
		num = $this.val()

		$.post('/product/updatecart', {
			'id': id,
			'num': num,
			'csrfmiddlewaretoken': '{{csrf_token}}'
		}, function (data) {

			location.reload();
		});
	})
});

function openForm() {
	document.getElementById("myForm").style.display = "block";
}

function openForm1() {
	document.getElementById("myForm-hai").style.display = "block";
}

function closeForm1() {
	document.getElementById("myForm-hai").style.display = "none";
}

function closeForm() {
	var ele = document.getElementsByName('gender');

	for (i = 0; i < ele.length; i++) {
		if (ele[i].checked)
			id = ele[i].value;
	}
	$.post('/cart/updateadd', {
		'id': id,
		'csrfmiddlewaretoken': '{{csrf_token}}'
	}, function (data) {
		location.reload();
	});
	document.getElementById("myForm").style.display = "none";
}