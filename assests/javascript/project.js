$(document).ready(function(){

    $.getJSON("/fetchallclgname",{ajax:true},function(data){
       $.each(data.data,function(index,item){
        // alert(data.data)
        // console.log(item)
       /*$('#clgname').empty()*/
       console.log($("#cid").val())
       if(item.id==$("#cid").val())
        {
            
            $('#clgname').append($('<option>').text(item.name).val(item.id))
            $('#clgname').attr("selected","selected");     
        }
        else{
            $('#clgname').append($('<option>').text(item.name).val(item.id))
        }
       
    
       })
    })




    $.getJSON("/fetchallstates",{ajax:true},function(data){
        
       
        $.each(data,function(index,item){
        /*$('#states').empty()*/
        alert(item.state_name)
        $('#states').append($('<option>').text(item.state_name).val(item.state_id))
     
        })
     })


})