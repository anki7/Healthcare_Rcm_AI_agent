export default {
  async fetch(request) {
    // Get the pathname from the request
    const url = new URL(request.url);
    const path = url.pathname;

    // Serve static assets (js, css, etc.) from the dist directory
    // If the path is for a static asset, serve it directly
    if (path.match(/\.(js|css|png|jpg|jpeg|gif|svg|ico|woff|woff2|ttf|eot)$/)) {
      return fetch(`https://healthcare-rcm-agent.pages.dev${path}`);
    }

    // For all other routes, serve the index.html (SPA routing)
    return fetch('https://healthcare-rcm-agent.pages.dev/index.html');
  }
}
EOFcd ~/healthcare-rcm-agent

# Create a worker directory
mkdir -p worker

# Create the worker script
cat > worker/index.js << 'EOF'
export default {
  async fetch(request) {
    // Get the pathname from the request
    const url = new URL(request.url);
    const path = url.pathname;

    // Serve static assets (js, css, etc.) from the dist directory
    // If the path is for a static asset, serve it directly
    if (path.match(/\.(js|css|png|jpg|jpeg|gif|svg|ico|woff|woff2|ttf|eot)$/)) {
      return fetch(`https://healthcare-rcm-agent.pages.dev${path}`);
    }

    // For all other routes, serve the index.html (SPA routing)
    return fetch('https://healthcare-rcm-agent.pages.dev/index.html');
  }
}
