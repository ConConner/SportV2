import Image from "next/image";
import styles from "./page.module.css";
import { json } from "stream/consumers";
import exp from "constants";
import Link from "next/link";


export default function Home() {
  return (
    <div className={styles.page}>
      <main className={styles.main}>
       Nur hier um zu existieren, gerne schnell überschreiben
       <Link href="/feats_results_page">Anzeige der Ergebnisse</Link>
      </main>
      <footer className={styles.footer}>
      </footer>
    </div>
  );
}