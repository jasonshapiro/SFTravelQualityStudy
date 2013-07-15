$(document).ready(function()
{

$('#hidden').hide();	

$('#togglediv').hover( function() {
	$('#togglebottom').filter(':not(:animated)').animate({top: '+=200'}, 200);
	$('#hidden').filter(':not(:animated)').fadeIn();
		},
	function() {
		$('#togglebottom').animate({top: '0'}, 200);
		$('#hidden').fadeOut(150);
	}
);
});