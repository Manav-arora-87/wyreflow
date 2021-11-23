$(document).ready(function(){

    $.getJSON("/fetchallclgname",{ajax:true},function(data){
       $.each(data.data,function(index,item){
        // alert(data.data)
        console.log(item)
       /*$('#clgname').empty()*/
       $('#clgname').append($('<option>').text(item.name).val(item.id))
    
       })
    })
})