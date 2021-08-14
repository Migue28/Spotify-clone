const Login = () => {
    return(
    <div class = "text-white flex items-center h-screen justify-center">
        <div class = "grid grid-flow-col grid-cols-1 grid-rows-4 gap-4 bg-gray-900 w-1/2 h-1/2 rounded-lg">
            <h1 class="text-3xl font-black mt-5 items-center">Spotify</h1>
            <p class="text-3xl font-black">Millions of songs.<br />Free on Spotify.</p>
            <div class="flex items-center justify-center">
            <button class="h-1/2 w-1/2 flex items-center justify-center text-lg font-bold bg-spotify-green rounded-full py-3 px-6">
                LOG IN
            </button>
            </div>
            <div class="flex items-center justify-center">
                <pre class="text-gray-400 font-bold">Don't have an account? </pre>
                <a href="/" class="text-white underline">SIGNUP</a>
            </div>
        </div>
    </div>
    )
}

export default Login;