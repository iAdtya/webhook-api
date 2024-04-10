"use client";
import { useEffect, useState } from "react";

const poll_data = () => {
  const [data, setData] = useState([]);
  const [polling, setPolling] = useState(false);

  useEffect(() => {
    const fetchData = async () => {
      setPolling(true);
      const response = await fetch("/api/data");
      const data = await response.json();
      setData(data);
      setTimeout(() => setPolling(false), 2000);
    };

    fetchData();
    const interval = setInterval(fetchData, 15000);
    return () => {
      clearInterval(interval);
      setPolling(false);
    };
  }, []);
  // console.log(data);

  return (
    <div className=" overflow-x-auto mt-20  ">
      {polling && <h1>Polling data...</h1>}
      <table className="table">
        <thead>
          <tr>
            <th>Author</th>
            <th>Action</th>
            <th>from_branch</th>
            <th>to_branch</th>
            <th>timestamp</th>
          </tr>
        </thead>
        <tbody>
          {data.map(
            (
              item: {
                author: string;
                action: string;
                from_branch: string;
                to_branch: string;
                timestamp: string;
              },
              index: number
            ) => (
              <tr key={index}>
                <td>{item.author}</td>
                <td>{item.action}</td>
                <td>{item.from_branch ? item.from_branch : "Empty!! "}</td>
                <td>{item.to_branch}</td>
                <td>{item.timestamp}</td>
              </tr>
            )
          )}
        </tbody>
      </table>
    </div>
  );
};

export default poll_data;
