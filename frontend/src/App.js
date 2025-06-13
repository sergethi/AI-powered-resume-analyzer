import ResumeUpload from "./components/ResumeUpload";


function App() {
  return (
    <div className="min-h-screen bg-gray-100 text-gray-800">
      <header className="bg-white shadow p-4 flex items-center justify-between">
        <h1 className="text-2xl font-bold text-blue-600">Resume Analyzer</h1>
        {/* <a
          className="text-sm text-blue-500 hover:underline"
          href="https://reactjs.org"
          target="_blank"
          rel="noopener noreferrer"
        >
          Learn React
        </a> */}
      </header>

      <main className="p-6 max-w-3xl mx-auto">
        <ResumeUpload />
      </main>
    </div>
  );
}

export default App;
