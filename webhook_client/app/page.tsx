import Image from "next/image";
import PollData from "./polling";
export default function Home() {
  return (
    <main className="flex flex-col min-h-screen absolute inset-0 h-full w-full bg-slate-900 bg-[linear-gradient(to_right,#80808012_1px,transparent_1px),linear-gradient(to_bottom,#80808012_1px,transparent_1px)] bg-[size:24px_24px] [mask-image:linear-gradient(to_top,transparent_0%,#000_70%)] ">
      <div className="flex justify-center mt-14">
        <div className="text-center max-w-2xl">
          <h1 className="text-5xl font-bold text-orange-400">
            Polling Data!!
          </h1>
        </div>
      </div>
      <PollData />
    </main>
  );
}
