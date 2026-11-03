import "./globals.css";
import { Inter, JetBrains_Mono } from "next/font/google";

const inter = Inter({ subsets: ["latin"], variable: "--font-inter", display: "swap" });
const mono = JetBrains_Mono({ subsets: ["latin"], variable: "--font-mono", display: "swap" });

export const metadata = {
  title: "Frontier Model Prompts - 107,250 Copy-Ready Prompts",
  description: "Interactive showcase for the Frontier Model Prompts library. Search and copy 9,750 Astra-tuned prompts across 39 categories, browse 11 frontier model packs, plus 3D pipeline, builds, and quickstarts."
};

export default function RootLayout({ children }) {
  return (
    <html lang="en">
      <body className={inter.variable + " " + mono.variable}>{children}</body>
    </html>
  );
}
