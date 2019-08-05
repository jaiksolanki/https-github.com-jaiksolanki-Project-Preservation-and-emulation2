$(document).ready(function(){
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
                        var bb=x[i].blackbook;
                        console.log(pid);
                        if(pid)
                        {    
                            addRow(pid,pname,status,ip,bb);     
                        }
                        else
                        {
                            var gid=x[i].Gid;
                            var sname=x[i].Sname;
                            var rollno=x[i].Rollno;
                            addRow1(gid,sname,rollno);
                        }
                }
            }
            
            
        }
    };
    xhttp.open("GET","http://127.0.0.1:5000/tdisplay",true);
    xhttp.send();
    
   

})

function addRow(pid,pname,status,ip,bb)
{
    var row=document.createElement("tr");
    var proj='<td class="mdl-data-table__cell--non-numeric">'+pname+'</td>';
    $(row).append(proj);
    var stat='<td class="mdl-data-table__cell--non-numeric">'+status+'</td>';
    $(row).append(stat);
    var bb='<td class="mdl-data-table__cell--non-numeric"><a target="_blank" class="mdl-navigation__link" href="'+bb+'" download>'+bb+'</a></td>';
    $(row).append(bb);
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
            a.setAttribute('class',"mdl-button mdl-js-button mdl-button--raised green mdl-js-ripple-effect mdl-button--colored mdl-color-text--white modal-trigger");
            form.setAttribute('action',"/tstart");
            form.setAttribute('method',"POST");
            var start = 'Start';
            $(a).append(start);
        }
        else if(status == 'Running')
        {        
            a.setAttribute('class',"mdl-button mdl-js-button mdl-button--raised red mdl-js-ripple-effect mdl-button--colored mdl-color-text--white modal-trigger");   
            form.setAttribute('action',"/tstop");
            form.setAttribute('method',"POST");
            var stop = 'Stop';
            $(a).append(stop);
        }
    $(form).append(hidden);    
    $(form).append(a);    
    $(tbtn).append(form);
    $(row).append(tbtn);
    $("tbody").append(row);
} 


function addRow1(gid,sname,rollno)
{
    var row=document.createElement("tr");
    var group='<td class="mdl-data-table__cell--non-numeric">'+gid+'</td>';
    $(row).append(group);
    var name='<td class="mdl-data-table__cell--non-numeric">'+sname+'</td>';
    $(row).append(name);
    var roll='<td class="mdl-data-table__cell--non-numeric">'+rollno+'</td>';
    $(row).append(roll);
    $("tfoot").append(row);
}