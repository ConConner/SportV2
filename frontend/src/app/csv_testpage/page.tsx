"use client";
import Image from "next/image";
import styles from "../page.module.css";
import { json } from "stream/consumers";
import exp from "constants";
import { MassExportButton, ExportCheckbox, SingleCSVExportButton } from "./csv_export_functions";
import { getAllAthletes, getAthleteById } from "../../../generic_functions/athlete_getters";




function CsvExporTable(){
let translatedTrainees=getAllAthletes();
let listItems = translatedTrainees.map(trainee=><li key={trainee.id}><ExportCheckbox id={trainee.id} /> {trainee.firstName}, {trainee.lastName} <SingleCSVExportButton id={trainee.id} vorName={trainee.vorName} nachName={trainee.nachName} /></li>);
return(<ul id='athleteTable'>{listItems}</ul>);
}


export default function Home() {
  return (
    <div className={styles.page}>
      <main className={styles.main}>
       Dies ist die CSV Export Testseite
        <div>
            <CsvExporTable />
            <MassExportButton />
        </div>
      </main>
      <footer className={styles.footer}>
      </footer>
    </div>
  );
}