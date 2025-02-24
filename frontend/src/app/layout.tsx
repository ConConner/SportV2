"use client"
import React, { ReactNode } from 'react'
import Link from "next/link";
import styles from "./page.module.css";
import { usePathname, useSearchParams } from 'next/navigation'


let sites: string[][] = [["Startseite", "/"], ["Testseite", "/test_page"] , ["CSV Testseite", "/csv_testpage"]];

function Nav_Menu() {
  const path = usePathname();
  let links = sites.map((site, index) => {
    if(site[1]==path){
      return<Link href={site[1]} key={index} className={styles.navbutt +" "+ styles.active}>{site[0]}</Link>
    }
    return<Link href={site[1]} key={index} className={styles.navbutt}>{site[0]}</Link>
  });
  return <nav key = 'navMen' className={styles.navbar}>{links}</nav>;
}


export default function RootLayout({
  children,
}: {
  children: React.ReactNode
}) {
  return (
    <html lang="de">
      <body>
        <div className={styles.back_layer}>
          <Nav_Menu />
          <div className={styles.page}>
            <main className={styles.main}>
              <div className={styles.content}>
                {children}
              </div>
            </main>
          </div>
        </div>
      </body>
    </html>
  )
}
