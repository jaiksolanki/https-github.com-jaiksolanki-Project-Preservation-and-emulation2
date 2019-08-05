$(document).ready(function(){
    var script=document.createElement('script');
    var src='<defer src="https://code.getmdl.io/1.3.0/material.min.js"></script>';
    $(script).src;
    $("tbody").empty();
    var xhttp=new XMLHttpRequest();
    
    xhttp.onreadystatechange = function() {
        if (this.readyState == 4 && this.status == 200) {
           // Typical action to be performed when the document is ready:
           var x = JSON.parse(xhttp.responseText);
           console.log(x);
           if(x!=null)
           {
                for (var i=0;i<x.length;i++)
                {  
                        var pid = x[i].Pid;
                        var pname=x[i].ProjectName;
                        var status=x[i].Pstatus;
                        var ip=x[i].ip;
                        addRow(pid,pname,status,ip);     
                }
            }
            
            
        }
    };
    xhttp.open("GET","http://127.0.0.1:5000/projects",true);
    xhttp.send();
    
   

})

function addRow(pid,pname,status,ip)
{
    var row=document.createElement("tr");
    var proj='<td class="mdl-data-table__cell--non-numeric">'+pname+'</td>';
    $(row).append(proj);
    var stat='<td class="mdl-data-table__cell--non-numeric">'+status+'</td>';
    $(row).append(stat);
    var ip='<td class="mdl-data-table__cell--non-numeric"><a target="_blank" class="mdl-navigation__link" href="'+ip+'">'+ip+'</a></td>';
    $(row).append(ip);

    var tbtn=document.createElement("td");
    var form = document.createElement("form");
    var hidden=document.createElement('input');
    hidden.setAttribute('id',pid);
    hidden.setAttribute('value',pid)
    hidden.setAttribute('name','pid')
    hidden.setAttribute('type','hidden')
    var a=document.createElement('button');
    if (status == 'Stopped')
    {   
        a.setAttribute('class',"mdl-button mdl-js-button mdl-button--raised mdl-js-ripple-effect green mdl-button--colored mdl-color-text--white modal-trigger");
        form.setAttribute('action',"/start");
        form.setAttribute('method',"POST");
        var start = 'Start';
        $(a).append(start);
    }
    else if(status == 'Running')
    {           
        a.setAttribute('class',"mdl-button mdl-js-button mdl-button--raised mdl-js-ripple-effect red mdl-button--colored mdl-color-text--white modal-trigger");
        form.setAttribute('action',"/stop");
        form.setAttribute('method',"POST");
        var stop = 'Stop';
        $(a).append(stop);
    }
    $(form).append(a);    
    $(form).append(hidden);
    $(tbtn).append(form);
    $(row).append(tbtn);

    var tbup=document.createElement("td");
    var updateform = document.createElement("form");
    var updatehidden=document.createElement('input');
    updatehidden.setAttribute('id',pid);
    updatehidden.setAttribute('value',pid)
    updatehidden.setAttribute('name','pid')
    updatehidden.setAttribute('type','hidden')
    var update=document.createElement('button');
    update.setAttribute('class',"mdl-button mdl-js-button mdl-button--raised mdl-js-ripple-effect mdl-button--colored mdl-color-text--white modal-trigger");
    updateform.setAttribute('action',"/update");
    updateform.setAttribute('method',"POST");
    var updatetext = 'Update';
    $(update).append(updatetext);
    $(updateform).append(update);    
    $(updateform).append(updatehidden);
    $(tbup).append(updateform);
    $(row).append(tbup);

    $("tbody").append(row);
} 

