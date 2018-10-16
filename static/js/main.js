function changetime(thisitem){
	var zone = $(thisitem).val();
    if(zone == "ist"){
        options = "<option value=''>Select Day</option>"+
                "<option value='mon'>Monday</option>"+
                "<option value='tue'>Tuesday </option>"+
                "<option value='wed'>Wednesday</option>"+
                "<option value='thu'>Thursday</option>"+
                "<option value='fri'>Friday </option>"+
                "<option value='sat'>Saturday</option>";
        $("#done").html(options);
        $("#dtwo").html(options);
        $("#tone").html("<option value=''>Select Time</option>");
        $("#tone").attr('disabled','disabled');
        $("#ttwo").html("<option value=''>Select Time</option>");
        $("#ttwo").attr('disabled','disabled');
    }
    else{
        options = "<option value=''>Select Day</option>"+
                "<option value='mon'>Monday</option>"+
                "<option value='tue'>Tuesday </option>"+
                "<option value='wed'>Wednesday</option>"+
                "<option value='thu'>Thursday</option>"+
                "<option value='fri'>Friday </option>"+
                "<option value='sat'>Saturday</option>"+
                "<option value='sun'>Sunday</option>";
        $("#done").html(options);
        $("#dtwo").html(options);
        $("#tone").html("<option value=''>Select Time</option>");
        $("#tone").attr('disabled','disabled');
        $("#ttwo").html("<option value=''>Select Time</option>");
        $("#ttwo").attr('disabled','disabled');
    }
	
}

$("#done").change(function() {
    zone = $("#zone").val();
    day = $("#done").val();
    if(day=="0" || day==null)
    {
        $("#tone").html("<option value=''>Select Time</option>");
        $("#tone").attr('disabled','disabled');
    }
    else{
        $.ajax({
            url: "daypreferences",
            type:"GET",
            data: {
               'zone':zone,
               'day':day,
            },
            success: function(response) {
                time = response.days
                options = "<option value=''>Select Time</option>";
                for ( i = 0; i < time.length; i++) {
                    options += "<option value='"+time[i]+"'>"+time[i]+"</option>";
                    
                }
                $("#tone").html(options);
                $("#tone").removeAttr('disabled');
            }
        });
    }
  
});

$("#dtwo").change(function() {
    zone = $("#zone").val();
    day = $("#dtwo").val();
    if(day=="0" || day==null)
    {
        $("#ttwo").html("<option value=''>Select Time</option>");
        $("#ttwo").attr('disabled','disabled');
    }
    else{
        $.ajax({
            url: "daypreferences",
            type:"GET",
            data: {
               'zone':zone,
               'day':day,
            },
            success: function(response) {
                time = response.days
                options = "<option value=''>Select Time</option>";
                for ( i = 0; i < time.length; i++) {
                    options += "<option value='"+time[i]+"'>"+time[i]+"</option>";
                    
                }
                $("#ttwo").html(options);
                $("#ttwo").removeAttr('disabled');
            }
        });
    }
  
});

//
$("#navbar-toggle").click(function(){
    $("#header-action-btn").toggleClass("active");
});

