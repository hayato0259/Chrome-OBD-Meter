//boot
setTimeout(function(){
	$('.boot img').css('display','flex');
	$('.boot img').css('width','60%');
	$('.boot img').css('opacity','1');
},1000);

setTimeout(function(){
     $('.boot img').css('opacity','0');
},3000);

setTimeout(function(){
     $('.boot').css('display','none');
	$('#speed').css('display','flex');
},5000);

//ゼロパディング
function zeroPadding(num,length){
    return ('0000000000' + num).slice(-length);
}