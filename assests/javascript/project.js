$(document).ready(function(){

    $.getJSON("/fetchallclgname",{ajax:true},function(data){
       $.each(data,function(index,item){
        alert(String(data))
        console.log(data)
       /*$('#clgname').empty()*/
       $('#clgname').append($('<option>').text(item[1]).val(item[0]))
    
       })
    })
})