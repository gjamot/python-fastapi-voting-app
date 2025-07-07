import { useEffect, useState } from "react";
import Post from "./types/Post";

const App: React.FC = () => {
  const [data, setData] = useState<Post | null>(null);

  useEffect(() => {
    fetch("/api/posts/1")
      .then((res) => res.json())
      .then(setData)
      .catch(console.error);
  }, []);

  return (
    <div>
      <h1>React JS | Python Fast API Voting APP</h1>
      {data ? <pre>{JSON.stringify(data, null, 2)}</pre> : <p>Loading data...</p>}
    </div>
  );
};

export default App;