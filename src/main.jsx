import React from 'react';
import { createRoot } from 'react-dom/client';
import { HeartHandshake, Home, CalendarDays, Phone, Mail, MapPin, ShieldCheck } from 'lucide-react';
import './style.css';

function App(){
  return <main>
    <header className="topbar">
      <div className="brand"><div className="logo">AD</div><div><strong>Acti'Dem</strong><span>Association · Site officiel</span></div></div>
      <nav><a href="#services">Services</a><a href="#brocante">Brocante 2026</a><a href="#contact">Contact</a></nav>
    </header>
    <section className="hero">
      <p className="badge">actidem.fr</p>
      <h1>Accompagner, débarrasser et aider avec humanité.</h1>
      <p>Acti'Dem accompagne les particuliers et professionnels autour du débarras, de l'entraide et des situations complexes, notamment le syndrome de Diogène.</p>
      <div className="actions"><a href="#contact">Nous contacter</a><a className="light" href="#brocante">Brocante d'Automne</a></div>
    </section>
    <section id="services" className="section"><h2>Nos actions</h2><div className="grid">
      <Card icon={<HeartHandshake/>} title="Accompagnement humain" text="Écoute, aide progressive et accompagnement adapté aux situations sensibles."/>
      <Card icon={<Home/>} title="Débarras" text="Débarras particuliers ou professionnels, tri, organisation et orientation."/>
      <Card icon={<ShieldCheck/>} title="Syndrome de Diogène" text="Approche respectueuse, discrète et organisée pour les situations complexes."/>
    </div></section>
    <section id="brocante" className="section event"><h2>Brocante d'Automne 2026</h2><p><CalendarDays/> 10 et 11 octobre 2026 · 09h00 à 18h00</p><p><MapPin/> Homécourt · chemin du Fond de la Noue</p><p>Animations, cochon à la broche, tombola, aires de jeux enfants et appel à venir déguisé.</p></section>
    <section id="contact" className="section contact"><h2>Contact</h2><p><Mail/> Adresse email à compléter</p><p><Phone/> Téléphone à compléter</p><p><MapPin/> Homécourt et environs</p></section>
    <footer>Acti'Dem · Site public en production · Données officielles pilotées par SharePoint</footer>
  </main>
}
function Card({icon,title,text}){return <article className="card">{icon}<h3>{title}</h3><p>{text}</p></article>}
createRoot(document.getElementById('root')).render(<App/>);
