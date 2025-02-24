let exportThese:Array<Number>;
exportThese =[];
import { getAthleteById } from "../../../generic_functions/athlete_getters";
import { Athlete } from "@/models/athlete";
function exportToCsv(idArray:Array<Number>){
  //get Actual Values for export from Database/API here
  console.log(idArray);
  let valueRows = Array<Array<string>>();
  let fullname = '';
  idArray.map((row) =>{
    let curId= Number(row);
    let athlete =getAthleteById(curId);
    fullname = athlete?.firstName + '_' + athlete?.lastName;
    let feats = athlete?.feats;
    if (feats == undefined ){
      valueRows.push( [
          String(athlete?.id),
          String(athlete?.lastName),
          String(athlete?.firstName),
          String(athlete?.sex),
          String(athlete?.eMail),
          String(athlete?.dateOfBirth),
          '',
          '',
          '',
          '',
          ''
      ]);
    } else{
      feats.forEach((feat) => {
        valueRows.push( [
          String(athlete?.id),
          String(athlete?.lastName),
          String(athlete?.firstName),
          String(athlete?.sex),
          String(athlete?.eMail),
          String(athlete?.dateOfBirth),
          String(feat.discipline),
          String(feat.exercise),
          String(feat.date),
          String(feat.result),
          String(feat.score)
        ]);
      });
    }
  });
  const csvRows = [
    ["ID", "LASTNAME", "NAME", "SEX", "EMAIL", "DATEOFBIRTH", "DISCIPLINE", "EXERCISE", "DATE", "RESULT", "SCORE"], // CSV headers
    valueRows.map((e) => e.join(";")) // CSV rows
  ];
  if(idArray.length<1){
    alert("Bitte wählen sie die Athleten aus, welche sie exportieren wollen!");
  }else{
    const csvContent = csvRows.map((e) => e.join(";")).join("\n");
    //get the current date in dd.mm.yyyy format
    let curDate: Date;
    curDate = new Date();
    let curDay: string;
    let curMonth: string;
    let curYear: string;
    curDay = String(curDate.getDate());
    curMonth = String(curDate.getMonth()+1);
    curYear = String(curDate.getFullYear());
    let dateString:String;
    dateString = curYear + '-' + curMonth + '-' + curDay;
    
    // Create a Blob and trigger download
    const blob = new Blob([csvContent], { type: "text/csv" });
    const url = URL.createObjectURL(blob);
    const link = document.createElement("a");
    link.href = url;
    if (idArray.length==1){
      link.download = `${fullname}_${dateString}.csv`;
    }else{
      link.download = `athleten_export_${dateString}.csv`;
    }
    link.click();
    URL.revokeObjectURL(url);
  }
}

export function  ExportCheckbox({id}){
  let willBeExported = false;
  function putID(yes:boolean, id:Number){
    willBeExported=!yes;
    if(willBeExported){
      exportThese.push(id);
    }else{
      exportThese=exportThese.filter(item=> item!=id);
    }
  }
  return(
  <input id = {`${id}export_checkbox`} name='csvCheckbox' type='checkbox' onChange={()=>putID(willBeExported, id)}></input>
  );
}

export function MassExportButton(){
  function massExport(){
    exportToCsv(exportThese);
  }
  return(
    <button name="csvMassExportButt" onClick = {()=>massExport()}>
        Alle ausgewählten als CSV exportieren
    </button>
    );
}

export function SingleCSVExportButton({id, vorName, nachName}){
  function exportAsCSV(id){
    let justThis:Array<Number>; 
    justThis =[id];
    exportToCsv(justThis);
  }
  return(
  <button id = {`${id}export_button`} name='csvSingleExportButt' onClick = {()=>exportAsCSV(id)}>
      {vorName} {nachName} als CSV exportieren
  </button>
  );
}