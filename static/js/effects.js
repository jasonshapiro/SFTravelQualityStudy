$(document).ready(function()
{

$('#hidden').hide();	

$('#togglediv').mouseenter( function() {
///	$('#togglebottom').filter(':not(:animated)').animate({top: '+=200'}, 200);
///	$('#hidden').filter(':not(:animated)').fadeIn();
	$('#togglebottom').stop().animate({'marginTop': '200px'}, 200);
	$('#hidden').fadeIn();
});

$('.navmenu').mouseleave(
	function() {
		$('#togglebottom').stop().animate({'marginTop': '0'}, 200);
		$('#hidden').stop().fadeOut(150);
	}
);
});