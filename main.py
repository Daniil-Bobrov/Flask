# noinspection PyUnresolvedReferences
from flask import Flask

app = Flask(__name__)


@app.route('/')
def index():
    return '''
<body>
    <div class="related" role="navigation" aria-label="related navigation">
      <h3>Navigation</h3>
      <ul>
        <li class="right" style="margin-right: 10px">
          <a href="../genindex/" title="General Index" accesskey="I">index</a></li>
        <li class="right">
          <a href="../py-modindex/" title="Python Module Index">modules</a> |</li>
        <li class="right">
          <a href="../tutorial/" title="Tutorial" accesskey="N">next</a> |</li>
        <li class="right">
          <a href="../installation/" title="Installation" accesskey="P">previous</a> |</li>
        <li class="nav-item nav-item-0"><a href="../">Flask Documentation (2.3.x)</a> »</li>
        <li class="nav-item nav-item-this"><a href="">Quickstart</a></li> 
      </ul>
    </div>  
    <div class="document">
    <p class="version-warning"><strong>Warning:</strong> This is the development version. The latest stable version is <a href="../../2.2.x/quickstart/">Version 2.2.x</a>.</p>
      <div class="documentwrapper">
        <div class="bodywrapper">
          <div class="body" role="main">

  <section id="quickstart">
<h1><a class="headerlink" href="#quickstart" title="Permalink to this headline">Quickstart</a></h1>
<p>Eager to get started? This page gives a good introduction to Flask.
Follow <a class="reference internal" href="../installation/"><span class="doc">Installation</span></a> to set up a project and install Flask first.</p>
<section id="a-minimal-application">
<h2><a class="headerlink" href="#a-minimal-application" title="Permalink to this headline">A Minimal Application</a></h2>
<p>A minimal Flask application looks something like this:</p>
<div class="highlight-python notranslate"><div class="highlight"><pre><span></span><span class="kn">from</span> <span class="nn">flask</span> <span class="kn">import</span> <span class="n">Flask</span>
<span class="n">app</span> <span class="o">=</span> <span class="n">Flask</span><span class="p">(</span><span class="vm">__name__</span><span class="p">)</span>
<span class="nd">@app</span><span class="o">.</span><span class="n">route</span><span class="p">(</span><span class="s2">"/"</span><span class="p">)</span>
<span class="k">def</span> <span class="nf">hello_world</span><span class="p">():</span>
    <span class="k">return</span> <span class="s2">"&lt;p&gt;Hello, World!&lt;/p&gt;"</span>
</pre></div>
</div>
<p>So what did that code do?</p>
<ol class="arabic simple">
<li><p>First we imported the <a class="reference internal" href="../api/#flask.Flask" title="flask.Flask"><code class="xref py py-class docutils literal notranslate"><span class="pre">Flask</span></code></a> class. An instance of
this class will be our WSGI application.</p></li>
<li><p>Next we create an instance of this class. The first argument is the
name of the application’s module or package. <code class="docutils literal notranslate"><span class="pre">__name__</span></code> is a
convenient shortcut for this that is appropriate for most cases.
This is needed so that Flask knows where to look for resources such
as templates and static files.</p></li>
<li><p>We then use the <a class="reference internal" href="../api/#flask.Flask.route" title="flask.Flask.route"><code class="xref py py-meth docutils literal notranslate"><span class="pre">route()</span></code></a> decorator to tell Flask
what URL should trigger our function.</p></li>
<li><p>The function returns the message we want to display in the user’s
browser. The default content type is HTML, so HTML in the string<br>
will be rendered by the browser.</p></li>
</ol>
<p>Save it as <code class="file docutils literal notranslate"><span class="pre">hello.py</span></code> or something similar. Make sure to not call
your application <code class="file docutils literal notranslate"><span class="pre">flask.py</span></code> because this would conflict with Flask
itself.</p>
<p>To run the application, use the <code class="docutils literal notranslate"><span class="pre">flask</span></code> command or
<code class="docutils literal notranslate"><span class="pre">python</span> <span class="pre">-m</span> <span class="pre">flask</span></code>. You need to tell the Flask where your application
is with the <code class="docutils literal notranslate"><span class="pre">--app</span></code> option.</p>
<div class="highlight-text notranslate"><div class="highlight"><pre><span></span>$ flask --app hello run
 * Serving Flask app 'hello'
 * Running on http://127.0.0.1:5000 (Press CTRL+C to quit)
</pre></div>
</div>
<div class="admonition-application-discovery-behavior admonition">
<p class="admonition-title">Application Discovery Behavior</p>
<p>As a shortcut, if the file is named <code class="docutils literal notranslate"><span class="pre">app.py</span></code> or <code class="docutils literal notranslate"><span class="pre">wsgi.py</span></code>, you
don’t have to use <code class="docutils literal notranslate"><span class="pre">--app</span></code>. See <a class="reference internal" href="../cli/"><span class="doc">Command Line Interface</span></a> for more details.</p>
</div>
<p>This launches a very simple builtin server, which is good enough for
testing but probably not what you want to use in production. For
deployment options see <a class="reference internal" href="../deploying/"><span class="doc">Deploying to Production</span></a>.</p>
<p>Now head over to <a class="reference external" href="http://127.0.0.1:5000/">http://127.0.0.1:5000/</a>, and you should see your hello
world greeting.</p>
<p>If another program is already using port 5000, you’ll see
<code class="docutils literal notranslate"><span class="pre">OSError:</span> <span class="pre">[Errno</span> <span class="pre">98]</span></code> or <code class="docutils literal notranslate"><span class="pre">OSError:</span> <span class="pre">[WinError</span> <span class="pre">10013]</span></code> when the
server tries to start. See <a class="reference internal" href="../server/#address-already-in-use"><span class="std std-ref">Address already in use</span></a> for how to
handle that.</p>
<div class="admonition-externally-visible-server admonition" id="public-server">
<p class="admonition-title">Externally Visible Server</p>
<p>If you run the server you will notice that the server is only accessible
from your own computer, not from any other in the network.  This is the
default because in debugging mode a user of the application can execute
arbitrary Python code on your computer.</p>
<p>If you have the debugger disabled or trust the users on your network,
you can make the server publicly available simply by adding
<code class="docutils literal notranslate"><span class="pre">--host=0.0.0.0</span></code> to the command line:</p>
<div class="highlight-default notranslate"><div class="highlight"><pre><span></span>$ flask run --host=0.0.0.0
</pre></div>
</div>
<p>This tells your operating system to listen on all public IPs.</p>
</div>
</section>
<section id="debug-mode">
<h2>Debug Mode<a class="headerlink" href="#debug-mode" title="Permalink to this headline">Debug Mode</a></h2>
<p>The <code class="docutils literal notranslate"><span class="pre">flask</span> <span class="pre">run</span></code> command can do more than just start the development
server. By enabling debug mode, the server will automatically reload if
code changes, and will show an interactive debugger in the browser if an
error occurs during a request.</p>
<img alt="The interactive debugger in action." class="screenshot align-center" src="../_images/debugger.png">
<div class="admonition warning">
<p class="admonition-title">Warning</p>
<p>The debugger allows executing arbitrary Python code from the
browser. It is protected by a pin, but still represents a major
security risk. Do not run the development server or debugger in a
production environment.</p>
</div>
<p>To enable debug mode, use the <code class="docutils literal notranslate"><span class="pre">--debug</span></code> option.</p>
<div class="highlight-text notranslate"><div class="highlight"><pre><span></span>$ flask --app hello --debug run
 * Serving Flask app 'hello'
 * Debug mode: on
 * Running on http://127.0.0.1:5000 (Press CTRL+C to quit)
 * Restarting with stat
 * Debugger is active!
 * Debugger PIN: nnn-nnn-nnn
</pre></div>
</div>
<p>See also:</p>
<ul class="simple">
<li><p><a class="reference internal" href="../server/"><span class="doc">Development Server</span></a> and <a class="reference internal" href="../cli/"><span class="doc">Command Line Interface</span></a> for information about running in debug mode.</p></li>
<li><p><a class="reference internal" href="../debugging/"><span class="doc">Debugging Application Errors</span></a> for information about using the built-in debugger
and other debuggers.</p></li>
<li><p><a class="reference internal" href="../logging/"><span class="doc">Logging</span></a> and <a class="reference internal" href="../errorhandling/"><span class="doc">Handling Application Errors</span></a> to log errors and display
nice error pages.</p></li>
</ul>
</section>
<section id="html-escaping">
<h2><a class="headerlink" href="#html-escaping" title="Permalink to this headline">HTML Escaping</a></h2>
<p>When returning HTML (the default response type in Flask), any
user-provided values rendered in the output must be escaped to protect
from injection attacks. HTML templates rendered with Jinja, introduced
later, will do this automatically.</p>
<p><code class="xref py py-func docutils literal notranslate"><span class="pre">escape()</span></code>, shown here, can be used manually. It is
omitted in most examples for brevity, but you should always be aware of
how you’re using untrusted data.</p>
<div class="highlight-python notranslate"><div class="highlight"><pre><span></span><span class="kn">from</span> <span class="nn">markupsafe</span> <span class="kn">import</span> <span class="n">escape</span>
<span class="nd">@app</span><span class="o">.</span><span class="n">route</span><span class="p">(</span><span class="s2">"/&lt;name&gt;"</span><span class="p">)</span>
<span class="k">def</span> <span class="nf">hello</span><span class="p">(</span><span class="n">name</span><span class="p">):</span>
    <span class="k">return</span> <span class="sa">f</span><span class="s2">"Hello, </span><span class="si">{</span><span class="n">escape</span><span class="p">(</span><span class="n">name</span><span class="p">)</span><span class="si">}</span><span class="s2">!"</span>
</pre></div>
</div>
<p>If a user managed to submit the name <code class="docutils literal notranslate"><span class="pre">&lt;script&gt;alert("bad")&lt;/script&gt;</span></code>,
escaping causes it to be rendered as text, rather than running the
script in the user’s browser.</p>
<p><code class="docutils literal notranslate"><span class="pre">&lt;name&gt;</span></code> in the route captures a value from the URL and passes it to
the view function. These variable rules are explained below.</p>
</section>
<section id="routing">
<h2><a class="headerlink" href="#routing" title="Permalink to this headline">Routing</a></h2>
<p>Modern web applications use meaningful URLs to help users. Users are more
likely to like a page and come back if the page uses a meaningful URL they can
remember and use to directly visit a page.</p>
<p>Use the <a class="reference internal" href="../api/#flask.Flask.route" title="flask.Flask.route"><code class="xref py py-meth docutils literal notranslate"><span class="pre">route()</span></code></a> decorator to bind a function to a URL.</p>
<div class="highlight-default notranslate"><div class="highlight"><pre><span></span><span class="nd">@app</span><span class="o">.</span><span class="n">route</span><span class="p">(</span><span class="s1">'/'</span><span class="p">)</span>
<span class="k">def</span> <span class="nf">index</span><span class="p">():</span>
    <span class="k">return</span> <span class="s1">'Index Page'</span>
<span class="nd">@app</span><span class="o">.</span><span class="n">route</span><span class="p">(</span><span class="s1">'/hello'</span><span class="p">)</span>
<span class="k">def</span> <span class="nf">hello</span><span class="p">():</span>
    <span class="k">return</span> <span class="s1">'Hello, World'</span>
</pre></div>
</div>
<p>You can do more! You can make parts of the URL dynamic and attach multiple
rules to a function.</p>
<section id="variable-rules">
<h3>Variable Rules<a class="headerlink" href="#variable-rules" title="Permalink to this headline">¶</a></h3>
<p>You can add variable sections to a URL by marking sections with
<code class="docutils literal notranslate"><span class="pre">&lt;variable_name&gt;</span></code>. Your function then receives the <code class="docutils literal notranslate"><span class="pre">&lt;variable_name&gt;</span></code>
as a keyword argument. Optionally, you can use a converter to specify the type
of the argument like <code class="docutils literal notranslate"><span class="pre">&lt;converter:variable_name&gt;</span></code>.</p>
<div class="highlight-default notranslate"><div class="highlight"><pre><span></span><span class="kn">from</span> <span class="nn">markupsafe</span> <span class="kn">import</span> <span class="n">escape</span>
<span class="nd">@app</span><span class="o">.</span><span class="n">route</span><span class="p">(</span><span class="s1">'/user/&lt;username&gt;'</span><span class="p">)</span>
<span class="k">def</span> <span class="nf">show_user_profile</span><span class="p">(</span><span class="n">username</span><span class="p">):</span>
    <span class="c1"># show the user profile for that user</span>
    <span class="k">return</span> <span class="sa">f</span><span class="s1">'User </span><span class="si">{</span><span class="n">escape</span><span class="p">(</span><span class="n">username</span><span class="p">)</span><span class="si">}</span><span class="s1">'</span>
<span class="nd">@app</span><span class="o">.</span><span class="n">route</span><span class="p">(</span><span class="s1">'/post/&lt;int:post_id&gt;'</span><span class="p">)</span>
<span class="k">def</span> <span class="nf">show_post</span><span class="p">(</span><span class="n">post_id</span><span class="p">):</span>
    <span class="c1"># show the post with the given id, the id is an integer</span>
    <span class="k">return</span> <span class="sa">f</span><span class="s1">'Post </span><span class="si">{</span><span class="n">post_id</span><span class="si">}</span><span class="s1">'</span>
<span class="nd">@app</span><span class="o">.</span><span class="n">route</span><span class="p">(</span><span class="s1">'/path/&lt;path:subpath&gt;'</span><span class="p">)</span>
<span class="k">def</span> <span class="nf">show_subpath</span><span class="p">(</span><span class="n">subpath</span><span class="p">):</span>
    <span class="c1"># show the subpath after /path/</span>
    <span class="k">return</span> <span class="sa">f</span><span class="s1">'Subpath </span><span class="si">{</span><span class="n">escape</span><span class="p">(</span><span class="n">subpath</span><span class="p">)</span><span class="si">}</span><span class="s1">'</span>
</pre></div>
</div>
<p>Converter types:</p>
<div class="wy-table-responsive"><table class="docutils align-default">
<colgroup>
<col style="width: 19%">
<col style="width: 81%">
</colgroup>
<tbody>
<tr class="row-odd"><td><p><code class="docutils literal notranslate"><span class="pre">string</span></code></p></td>
<td><p>(default) accepts any text without a slash</p></td>
</tr>
<tr class="row-even"><td><p><code class="docutils literal notranslate"><span class="pre">int</span></code></p></td>
<td><p>accepts positive integers</p></td>
</tr>
<tr class="row-odd"><td><p><code class="docutils literal notranslate"><span class="pre">float</span></code></p></td>
<td><p>accepts positive floating point values</p></td>
</tr>
<tr class="row-even"><td><p><code class="docutils literal notranslate"><span class="pre">path</span></code></p></td>
<td><p>like <code class="docutils literal notranslate"><span class="pre">string</span></code> but also accepts slashes</p></td>
</tr>
<tr class="row-odd"><td><p><code class="docutils literal notranslate"><span class="pre">uuid</span></code></p></td>
<td><p>accepts UUID strings</p></td>
</tr>
</tbody>
</table></div>
</section>
<section id="unique-urls-redirection-behavior">
<h3>Unique URLs / Redirection Behavior<a class="headerlink" href="#unique-urls-redirection-behavior" title="Permalink to this headline">¶</a></h3>
<p>The following two rules differ in their use of a trailing slash.</p>
<div class="highlight-default notranslate"><div class="highlight"><pre><span></span><span class="nd">@app</span><span class="o">.</span><span class="n">route</span><span class="p">(</span><span class="s1">'/projects/'</span><span class="p">)</span>
<span class="k">def</span> <span class="nf">projects</span><span class="p">():</span>
    <span class="k">return</span> <span class="s1">'The project page'</span>
<span class="nd">@app</span><span class="o">.</span><span class="n">route</span><span class="p">(</span><span class="s1">'/about'</span><span class="p">)</span>
<span class="k">def</span> <span class="nf">about</span><span class="p">():</span>
    <span class="k">return</span> <span class="s1">'The about page'</span>
</pre></div>
</div>
<p>The canonical URL for the <code class="docutils literal notranslate"><span class="pre">projects</span></code> endpoint has a trailing slash.
It’s similar to a folder in a file system. If you access the URL without
a trailing slash (<code class="docutils literal notranslate"><span class="pre">/projects</span></code>), Flask redirects you to the canonical URL
with the trailing slash (<code class="docutils literal notranslate"><span class="pre">/projects/</span></code>).</p>
<p>The canonical URL for the <code class="docutils literal notranslate"><span class="pre">about</span></code> endpoint does not have a trailing
slash. It’s similar to the pathname of a file. Accessing the URL with a
trailing slash (<code class="docutils literal notranslate"><span class="pre">/about/</span></code>) produces a 404 “Not Found” error. This helps
keep URLs unique for these resources, which helps search engines avoid
indexing the same page twice.</p>
</section>
<section id="url-building">
<span id="id1"></span><h3>URL Building<a class="headerlink" href="#url-building" title="Permalink to this headline">¶</a></h3>
<p>To build a URL to a specific function, use the <a class="reference internal" href="../api/#flask.url_for" title="flask.url_for"><code class="xref py py-func docutils literal notranslate"><span class="pre">url_for()</span></code></a> function.
It accepts the name of the function as its first argument and any number of
keyword arguments, each corresponding to a variable part of the URL rule.
Unknown variable parts are appended to the URL as query parameters.</p>
<p>Why would you want to build URLs using the URL reversing function
<a class="reference internal" href="../api/#flask.url_for" title="flask.url_for"><code class="xref py py-func docutils literal notranslate"><span class="pre">url_for()</span></code></a> instead of hard-coding them into your templates?</p>
<ol class="arabic simple">
<li><p>Reversing is often more descriptive than hard-coding the URLs.</p></li>
<li><p>You can change your URLs in one go instead of needing to remember to
manually change hard-coded URLs.</p></li>
<li><p>URL building handles escaping of special characters transparently.</p></li>
<li><p>The generated paths are always absolute, avoiding unexpected behavior
of relative paths in browsers.</p></li>
<li><p>If your application is placed outside the URL root, for example, in
<code class="docutils literal notranslate"><span class="pre">/myapplication</span></code> instead of <code class="docutils literal notranslate"><span class="pre">/</span></code>, <a class="reference internal" href="../api/#flask.url_for" title="flask.url_for"><code class="xref py py-func docutils literal notranslate"><span class="pre">url_for()</span></code></a> properly
handles that for you.</p></li>
</ol>
<p>For example, here we use the <a class="reference internal" href="../api/#flask.Flask.test_request_context" title="flask.Flask.test_request_context"><code class="xref py py-meth docutils literal notranslate"><span class="pre">test_request_context()</span></code></a> method
to try out <a class="reference internal" href="../api/#flask.url_for" title="flask.url_for"><code class="xref py py-func docutils literal notranslate"><span class="pre">url_for()</span></code></a>. <a class="reference internal" href="../api/#flask.Flask.test_request_context" title="flask.Flask.test_request_context"><code class="xref py py-meth docutils literal notranslate"><span class="pre">test_request_context()</span></code></a>
tells Flask to behave as though it’s handling a request even while we use a
Python shell. See <a class="reference internal" href="#context-locals"><span class="std std-ref">Context Locals</span></a>.</p>
<div class="highlight-python notranslate"><div class="highlight"><pre><span></span><span class="kn">from</span> <span class="nn">flask</span> <span class="kn">import</span> <span class="n">url_for</span>
<span class="nd">@app</span><span class="o">.</span><span class="n">route</span><span class="p">(</span><span class="s1">'/'</span><span class="p">)</span>
<span class="k">def</span> <span class="nf">index</span><span class="p">():</span>
    <span class="k">return</span> <span class="s1">'index'</span>
<span class="nd">@app</span><span class="o">.</span><span class="n">route</span><span class="p">(</span><span class="s1">'/login'</span><span class="p">)</span>
<span class="k">def</span> <span class="nf">login</span><span class="p">():</span>
    <span class="k">return</span> <span class="s1">'login'</span>
<span class="nd">@app</span><span class="o">.</span><span class="n">route</span><span class="p">(</span><span class="s1">'/user/&lt;username&gt;'</span><span class="p">)</span>
<span class="k">def</span> <span class="nf">profile</span><span class="p">(</span><span class="n">username</span><span class="p">):</span>
    <span class="k">return</span> <span class="sa">f</span><span class="s1">'</span><span class="si">{</span><span class="n">username</span><span class="si">}</span><span class="se">\'</span><span class="s1">s profile'</span>
<span class="k">with</span> <span class="n">app</span><span class="o">.</span><span class="n">test_request_context</span><span class="p">():</span>
    <span class="nb">print</span><span class="p">(</span><span class="n">url_for</span><span class="p">(</span><span class="s1">'index'</span><span class="p">))</span>
    <span class="nb">print</span><span class="p">(</span><span class="n">url_for</span><span class="p">(</span><span class="s1">'login'</span><span class="p">))</span>
    <span class="nb">print</span><span class="p">(</span><span class="n">url_for</span><span class="p">(</span><span class="s1">'login'</span><span class="p">,</span> <span class="nb">next</span><span class="o">=</span><span class="s1">'/'</span><span class="p">))</span>
    <span class="nb">print</span><span class="p">(</span><span class="n">url_for</span><span class="p">(</span><span class="s1">'profile'</span><span class="p">,</span> <span class="n">username</span><span class="o">=</span><span class="s1">'John Doe'</span><span class="p">))</span>
</pre></div>
</div>
<div class="highlight-text notranslate"><div class="highlight"><pre><span></span>/
/login
/login?next=/
/user/John%20Doe
</pre></div>
</div>
</section>
<section id="http-methods">
<h3>HTTP Methods<a class="headerlink" href="#http-methods" title="Permalink to this headline">¶</a></h3>
<p>Web applications use different HTTP methods when accessing URLs. You should
familiarize yourself with the HTTP methods as you work with Flask. By default,
a route only answers to <code class="docutils literal notranslate"><span class="pre">GET</span></code> requests. You can use the <code class="docutils literal notranslate"><span class="pre">methods</span></code> argument
of the <a class="reference internal" href="../api/#flask.Flask.route" title="flask.Flask.route"><code class="xref py py-meth docutils literal notranslate"><span class="pre">route()</span></code></a> decorator to handle different HTTP methods.</p>
<div class="highlight-default notranslate"><div class="highlight"><pre><span></span><span class="kn">from</span> <span class="nn">flask</span> <span class="kn">import</span> <span class="n">request</span>
<span class="nd">@app</span><span class="o">.</span><span class="n">route</span><span class="p">(</span><span class="s1">'/login'</span><span class="p">,</span> <span class="n">methods</span><span class="o">=</span><span class="p">[</span><span class="s1">'GET'</span><span class="p">,</span> <span class="s1">'POST'</span><span class="p">])</span>
<span class="k">def</span> <span class="nf">login</span><span class="p">():</span>
    <span class="k">if</span> <span class="n">request</span><span class="o">.</span><span class="n">method</span> <span class="o">==</span> <span class="s1">'POST'</span><span class="p">:</span>
        <span class="k">return</span> <span class="n">do_the_login</span><span class="p">()</span>
    <span class="k">else</span><span class="p">:</span>
        <span class="k">return</span> <span class="n">show_the_login_form</span><span class="p">()</span>
</pre></div>
</div>
<p>The example above keeps all methods for the route within one function,
which can be useful if each part uses some common data.</p>
<p>You can also separate views for different methods into different
functions. Flask provides a shortcut for decorating such routes with
<a class="reference internal" href="../api/#flask.Flask.get" title="flask.Flask.get"><code class="xref py py-meth docutils literal notranslate"><span class="pre">get()</span></code></a>, <a class="reference internal" href="../api/#flask.Flask.post" title="flask.Flask.post"><code class="xref py py-meth docutils literal notranslate"><span class="pre">post()</span></code></a>, etc. for each
common HTTP method.</p>
<div class="highlight-python notranslate"><div class="highlight"><pre><span></span><span class="nd">@app</span><span class="o">.</span><span class="n">get</span><span class="p">(</span><span class="s1">'/login'</span><span class="p">)</span>
<span class="k">def</span> <span class="nf">login_get</span><span class="p">():</span>
    <span class="k">return</span> <span class="n">show_the_login_form</span><span class="p">()</span>
<span class="nd">@app</span><span class="o">.</span><span class="n">post</span><span class="p">(</span><span class="s1">'/login'</span><span class="p">)</span>
<span class="k">def</span> <span class="nf">login_post</span><span class="p">():</span>
    <span class="k">return</span> <span class="n">do_the_login</span><span class="p">()</span>
</pre></div>
</div>
<p>If <code class="docutils literal notranslate"><span class="pre">GET</span></code> is present, Flask automatically adds support for the <code class="docutils literal notranslate"><span class="pre">HEAD</span></code> method
and handles <code class="docutils literal notranslate"><span class="pre">HEAD</span></code> requests according to the <a class="reference external" href="https://www.ietf.org/rfc/rfc2068.txt">HTTP RFC</a>. Likewise,
<code class="docutils literal notranslate"><span class="pre">OPTIONS</span></code> is automatically implemented for you.</p>
</section>
</section>
<section id="static-files">
<h2>Static Files<a class="headerlink" href="#static-files" title="Permalink to this headline">¶</a></h2>
<p>Dynamic web applications also need static files.  That’s usually where
the CSS and JavaScript files are coming from.  Ideally your web server is
configured to serve them for you, but during development Flask can do that
as well.  Just create a folder called <code class="file docutils literal notranslate"><span class="pre">static</span></code> in your package or next to
your module and it will be available at <code class="docutils literal notranslate"><span class="pre">/static</span></code> on the application.</p>
<p>To generate URLs for static files, use the special <code class="docutils literal notranslate"><span class="pre">'static'</span></code> endpoint name:</p>
<div class="highlight-default notranslate"><div class="highlight"><pre><span></span><span class="n">url_for</span><span class="p">(</span><span class="s1">'static'</span><span class="p">,</span> <span class="n">filename</span><span class="o">=</span><span class="s1">'style.css'</span><span class="p">)</span>
</pre></div>
</div>
<p>The file has to be stored on the filesystem as <code class="file docutils literal notranslate"><span class="pre">static/style.css</span></code>.</p>
</section>
<section id="rendering-templates">
<h2>Rendering Templates<a class="headerlink" href="#rendering-templates" title="Permalink to this headline">¶</a></h2>
<p>Generating HTML from within Python is not fun, and actually pretty
cumbersome because you have to do the HTML escaping on your own to keep
the application secure.  Because of that Flask configures the <a class="reference external" href="https://palletsprojects.com/p/jinja/">Jinja2</a> template engine for you automatically.</p>
<p>Templates can be used to generate any type of text file. For web applications, you’ll
primarily be generating HTML pages, but you can also generate markdown, plain text for
emails, any anything else.</p>
<p>For a reference to HTML, CSS, and other web APIs, use the <a class="reference external" href="https://developer.mozilla.org/">MDN Web Docs</a>.</p>
<p>To render a template you can use the <a class="reference internal" href="../api/#flask.render_template" title="flask.render_template"><code class="xref py py-func docutils literal notranslate"><span class="pre">render_template()</span></code></a>
method.  All you have to do is provide the name of the template and the
variables you want to pass to the template engine as keyword arguments.
Here’s a simple example of how to render a template:</p>
<div class="highlight-default notranslate"><div class="highlight"><pre><span></span><span class="kn">from</span> <span class="nn">flask</span> <span class="kn">import</span> <span class="n">render_template</span>
<span class="nd">@app</span><span class="o">.</span><span class="n">route</span><span class="p">(</span><span class="s1">'/hello/'</span><span class="p">)</span>
<span class="nd">@app</span><span class="o">.</span><span class="n">route</span><span class="p">(</span><span class="s1">'/hello/&lt;name&gt;'</span><span class="p">)</span>
<span class="k">def</span> <span class="nf">hello</span><span class="p">(</span><span class="n">name</span><span class="o">=</span><span class="kc">None</span><span class="p">):</span>
    <span class="k">return</span> <span class="n">render_template</span><span class="p">(</span><span class="s1">'hello.html'</span><span class="p">,</span> <span class="n">name</span><span class="o">=</span><span class="n">name</span><span class="p">)</span>
</pre></div>
</div>
<p>Flask will look for templates in the <code class="file docutils literal notranslate"><span class="pre">templates</span></code> folder.  So if your
application is a module, this folder is next to that module, if it’s a
package it’s actually inside your package:</p>
<p><strong>Case 1</strong>: a module:</p>
<div class="highlight-default notranslate"><div class="highlight"><pre><span></span><span class="o">/</span><span class="n">application</span><span class="o">.</span><span class="n">py</span>
<span class="o">/</span><span class="n">templates</span>
    <span class="o">/</span><span class="n">hello</span><span class="o">.</span><span class="n">html</span>
</pre></div>
</div>
<p><strong>Case 2</strong>: a package:</p>
<div class="highlight-default notranslate"><div class="highlight"><pre><span></span><span class="o">/</span><span class="n">application</span>
    <span class="o">/</span><span class="fm">__init__</span><span class="o">.</span><span class="n">py</span>
    <span class="o">/</span><span class="n">templates</span>
        <span class="o">/</span><span class="n">hello</span><span class="o">.</span><span class="n">html</span>
</pre></div>
</div>
<p>For templates you can use the full power of Jinja2 templates.  Head over
to the official <a class="reference external" href="https://jinja.palletsprojects.com/templates/">Jinja2 Template Documentation</a> for more information.</p>
<p>Here is an example template:</p>
<div class="highlight-html+jinja notranslate"><div class="highlight"><pre><span></span><span class="cp">&lt;!doctype html&gt;</span>
<span class="p">&lt;</span><span class="nt">title</span><span class="p">&gt;</span>Hello from Flask<span class="p">&lt;/</span><span class="nt">title</span><span class="p">&gt;</span>
<span class="cp">{%</span> <span class="k">if</span> <span class="nv">name</span> <span class="cp">%}</span>
  <span class="p">&lt;</span><span class="nt">h1</span><span class="p">&gt;</span>Hello <span class="cp">{{</span> <span class="nv">name</span> <span class="cp">}}</span>!<span class="p">&lt;/</span><span class="nt">h1</span><span class="p">&gt;</span>
<span class="cp">{%</span> <span class="k">else</span> <span class="cp">%}</span>
  <span class="p">&lt;</span><span class="nt">h1</span><span class="p">&gt;</span>Hello, World!<span class="p">&lt;/</span><span class="nt">h1</span><span class="p">&gt;</span>
<span class="cp">{%</span> <span class="k">endif</span> <span class="cp">%}</span>
</pre></div>
</div>
<p>Inside templates you also have access to the <a class="reference internal" href="../api/#flask.Flask.config" title="flask.Flask.config"><code class="xref py py-data docutils literal notranslate"><span class="pre">config</span></code></a>,
<a class="reference internal" href="../api/#flask.request" title="flask.request"><code class="xref py py-class docutils literal notranslate"><span class="pre">request</span></code></a>, <a class="reference internal" href="../api/#flask.session" title="flask.session"><code class="xref py py-class docutils literal notranslate"><span class="pre">session</span></code></a> and <a class="reference internal" href="../api/#flask.g" title="flask.g"><code class="xref py py-class docutils literal notranslate"><span class="pre">g</span></code></a> <a class="footnote-reference brackets" href="#id3" id="id2">1</a> objects
as well as the <a class="reference internal" href="../api/#flask.url_for" title="flask.url_for"><code class="xref py py-func docutils literal notranslate"><span class="pre">url_for()</span></code></a> and <a class="reference internal" href="../api/#flask.get_flashed_messages" title="flask.get_flashed_messages"><code class="xref py py-func docutils literal notranslate"><span class="pre">get_flashed_messages()</span></code></a> functions.</p>
<p>Templates are especially useful if inheritance is used.  If you want to
know how that works, see <a class="reference internal" href="../patterns/templateinheritance/"><span class="doc">Template Inheritance</span></a>. Basically
template inheritance makes it possible to keep certain elements on each
page (like header, navigation and footer).</p>
<p>Automatic escaping is enabled, so if <code class="docutils literal notranslate"><span class="pre">name</span></code> contains HTML it will be escaped
automatically.  If you can trust a variable and you know that it will be
safe HTML (for example because it came from a module that converts wiki
markup to HTML) you can mark it as safe by using the
<a class="reference internal" href="../api/#flask.Markup" title="markupsafe.Markup"><code class="xref py py-class docutils literal notranslate"><span class="pre">Markup</span></code></a> class or by using the <code class="docutils literal notranslate"><span class="pre">|safe</span></code> filter in the
template.  Head over to the Jinja 2 documentation for more examples.</p>
<p>Here is a basic introduction to how the <a class="reference internal" href="../api/#flask.Markup" title="markupsafe.Markup"><code class="xref py py-class docutils literal notranslate"><span class="pre">Markup</span></code></a> class works:</p>
<div class="highlight-default notranslate"><div class="highlight"><pre><span></span><span class="gp">&gt;&gt;&gt; </span><span class="kn">from</span> <span class="nn">markupsafe</span> <span class="kn">import</span> <span class="n">Markup</span>
<span class="gp">&gt;&gt;&gt; </span><span class="n">Markup</span><span class="p">(</span><span class="s1">'&lt;strong&gt;Hello </span><span class="si">%s</span><span class="s1">!&lt;/strong&gt;'</span><span class="p">)</span> <span class="o">%</span> <span class="s1">'&lt;blink&gt;hacker&lt;/blink&gt;'</span>
<span class="go">Markup('&lt;strong&gt;Hello &amp;lt;blink&amp;gt;hacker&amp;lt;/blink&amp;gt;!&lt;/strong&gt;')</span>
<span class="gp">&gt;&gt;&gt; </span><span class="n">Markup</span><span class="o">.</span><span class="n">escape</span><span class="p">(</span><span class="s1">'&lt;blink&gt;hacker&lt;/blink&gt;'</span><span class="p">)</span>
<span class="go">Markup('&amp;lt;blink&amp;gt;hacker&amp;lt;/blink&amp;gt;')</span>
<span class="gp">&gt;&gt;&gt; </span><span class="n">Markup</span><span class="p">(</span><span class="s1">'&lt;em&gt;Marked up&lt;/em&gt; &amp;raquo; HTML'</span><span class="p">)</span><span class="o">.</span><span class="n">striptags</span><span class="p">()</span>
<span class="go">'Marked up » HTML'</span>
</pre></div>
</div>
<details class="changelog">
<summary>Changelog</summary><div class="versionchanged">
<p><span class="versionmodified changed">Changed in version 0.5: </span>Autoescaping is no longer enabled for all templates.  The following
extensions for templates trigger autoescaping: <code class="docutils literal notranslate"><span class="pre">.html</span></code>, <code class="docutils literal notranslate"><span class="pre">.htm</span></code>,
<code class="docutils literal notranslate"><span class="pre">.xml</span></code>, <code class="docutils literal notranslate"><span class="pre">.xhtml</span></code>.  Templates loaded from a string will have
autoescaping disabled.</p>
</div>
</details><dl class="footnote brackets">
<dt class="label" id="id3"><span class="brackets"><a class="fn-backref" href="#id2">1</a></span></dt>
<dd><p>Unsure what that <a class="reference internal" href="../api/#flask.g" title="flask.g"><code class="xref py py-class docutils literal notranslate"><span class="pre">g</span></code></a> object is? It’s something in which
you can store information for your own needs. See the documentation
for <a class="reference internal" href="../api/#flask.g" title="flask.g"><code class="xref py py-class docutils literal notranslate"><span class="pre">flask.g</span></code></a> and <a class="reference internal" href="../patterns/sqlite3/"><span class="doc">Using SQLite 3 with Flask</span></a>.</p>
</dd>
</dl>
</section>
<section id="accessing-request-data">
<h2>Accessing Request Data<a class="headerlink" href="#accessing-request-data" title="Permalink to this headline">¶</a></h2>
<p>For web applications it’s crucial to react to the data a client sends to
the server.  In Flask this information is provided by the global
<a class="reference internal" href="../api/#flask.request" title="flask.request"><code class="xref py py-class docutils literal notranslate"><span class="pre">request</span></code></a> object.  If you have some experience with Python
you might be wondering how that object can be global and how Flask
manages to still be threadsafe.  The answer is context locals:</p>
<section id="context-locals">
<span id="id4"></span><h3>Context Locals<a class="headerlink" href="#context-locals" title="Permalink to this headline">¶</a></h3>
<div class="admonition-insider-information admonition">
<p class="admonition-title">Insider Information</p>
<p>If you want to understand how that works and how you can implement
tests with context locals, read this section, otherwise just skip it.</p>
</div>
<p>Certain objects in Flask are global objects, but not of the usual kind.
These objects are actually proxies to objects that are local to a specific
context.  What a mouthful.  But that is actually quite easy to understand.</p>
<p>Imagine the context being the handling thread.  A request comes in and the
web server decides to spawn a new thread (or something else, the
underlying object is capable of dealing with concurrency systems other
than threads).  When Flask starts its internal request handling it
figures out that the current thread is the active context and binds the
current application and the WSGI environments to that context (thread).
It does that in an intelligent way so that one application can invoke another
application without breaking.</p>
<p>So what does this mean to you?  Basically you can completely ignore that
this is the case unless you are doing something like unit testing.  You
will notice that code which depends on a request object will suddenly break
because there is no request object.  The solution is creating a request
object yourself and binding it to the context.  The easiest solution for
unit testing is to use the <a class="reference internal" href="../api/#flask.Flask.test_request_context" title="flask.Flask.test_request_context"><code class="xref py py-meth docutils literal notranslate"><span class="pre">test_request_context()</span></code></a>
context manager.  In combination with the <code class="docutils literal notranslate"><span class="pre">with</span></code> statement it will bind a
test request so that you can interact with it.  Here is an example:</p>
<div class="highlight-default notranslate"><div class="highlight"><pre><span></span><span class="kn">from</span> <span class="nn">flask</span> <span class="kn">import</span> <span class="n">request</span>
<span class="k">with</span> <span class="n">app</span><span class="o">.</span><span class="n">test_request_context</span><span class="p">(</span><span class="s1">'/hello'</span><span class="p">,</span> <span class="n">method</span><span class="o">=</span><span class="s1">'POST'</span><span class="p">):</span>
    <span class="c1"># now you can do something with the request until the</span>
    <span class="c1"># end of the with block, such as basic assertions:</span>
    <span class="k">assert</span> <span class="n">request</span><span class="o">.</span><span class="n">path</span> <span class="o">==</span> <span class="s1">'/hello'</span>
    <span class="k">assert</span> <span class="n">request</span><span class="o">.</span><span class="n">method</span> <span class="o">==</span> <span class="s1">'POST'</span>
</pre></div>
</div>
<p>The other possibility is passing a whole WSGI environment to the
<a class="reference internal" href="../api/#flask.Flask.request_context" title="flask.Flask.request_context"><code class="xref py py-meth docutils literal notranslate"><span class="pre">request_context()</span></code></a> method:</p>
<div class="highlight-default notranslate"><div class="highlight"><pre><span></span><span class="k">with</span> <span class="n">app</span><span class="o">.</span><span class="n">request_context</span><span class="p">(</span><span class="n">environ</span><span class="p">):</span>
    <span class="k">assert</span> <span class="n">request</span><span class="o">.</span><span class="n">method</span> <span class="o">==</span> <span class="s1">'POST'</span>
</pre></div>
</div>
</section>
<section id="the-request-object">
<h3>The Request Object<a class="headerlink" href="#the-request-object" title="Permalink to this headline">¶</a></h3>
<p>The request object is documented in the API section and we will not cover
it here in detail (see <a class="reference internal" href="../api/#flask.Request" title="flask.Request"><code class="xref py py-class docutils literal notranslate"><span class="pre">Request</span></code></a>). Here is a broad overview of
some of the most common operations.  First of all you have to import it from
the <code class="docutils literal notranslate"><span class="pre">flask</span></code> module:</p>
<div class="highlight-default notranslate"><div class="highlight"><pre><span></span><span class="kn">from</span> <span class="nn">flask</span> <span class="kn">import</span> <span class="n">request</span>
</pre></div>
</div>
<p>The current request method is available by using the
<a class="reference internal" href="../api/#flask.Request.method" title="flask.Request.method"><code class="xref py py-attr docutils literal notranslate"><span class="pre">method</span></code></a> attribute.  To access form data (data
transmitted in a <code class="docutils literal notranslate"><span class="pre">POST</span></code> or <code class="docutils literal notranslate"><span class="pre">PUT</span></code> request) you can use the
<a class="reference internal" href="../api/#flask.Request.form" title="flask.Request.form"><code class="xref py py-attr docutils literal notranslate"><span class="pre">form</span></code></a> attribute.  Here is a full example of the two
attributes mentioned above:</p>
<div class="highlight-default notranslate"><div class="highlight"><pre><span></span><span class="nd">@app</span><span class="o">.</span><span class="n">route</span><span class="p">(</span><span class="s1">'/login'</span><span class="p">,</span> <span class="n">methods</span><span class="o">=</span><span class="p">[</span><span class="s1">'POST'</span><span class="p">,</span> <span class="s1">'GET'</span><span class="p">])</span>
<span class="k">def</span> <span class="nf">login</span><span class="p">():</span>
    <span class="n">error</span> <span class="o">=</span> <span class="kc">None</span>
    <span class="k">if</span> <span class="n">request</span><span class="o">.</span><span class="n">method</span> <span class="o">==</span> <span class="s1">'POST'</span><span class="p">:</span>
        <span class="k">if</span> <span class="n">valid_login</span><span class="p">(</span><span class="n">request</span><span class="o">.</span><span class="n">form</span><span class="p">[</span><span class="s1">'username'</span><span class="p">],</span>
                       <span class="n">request</span><span class="o">.</span><span class="n">form</span><span class="p">[</span><span class="s1">'password'</span><span class="p">]):</span>
            <span class="k">return</span> <span class="n">log_the_user_in</span><span class="p">(</span><span class="n">request</span><span class="o">.</span><span class="n">form</span><span class="p">[</span><span class="s1">'username'</span><span class="p">])</span>
        <span class="k">else</span><span class="p">:</span>
            <span class="n">error</span> <span class="o">=</span> <span class="s1">'Invalid username/password'</span>
    <span class="c1"># the code below is executed if the request method</span>
    <span class="c1"># was GET or the credentials were invalid</span>
    <span class="k">return</span> <span class="n">render_template</span><span class="p">(</span><span class="s1">'login.html'</span><span class="p">,</span> <span class="n">error</span><span class="o">=</span><span class="n">error</span><span class="p">)</span>
</pre></div>
</div>
<p>What happens if the key does not exist in the <code class="docutils literal notranslate"><span class="pre">form</span></code> attribute?  In that
case a special <a class="reference external" href="https://docs.python.org/3/library/exceptions.html#KeyError" title="(in Python v3.10)"><code class="xref py py-exc docutils literal notranslate"><span class="pre">KeyError</span></code></a> is raised.  You can catch it like a
standard <a class="reference external" href="https://docs.python.org/3/library/exceptions.html#KeyError" title="(in Python v3.10)"><code class="xref py py-exc docutils literal notranslate"><span class="pre">KeyError</span></code></a> but if you don’t do that, a HTTP 400 Bad Request
error page is shown instead.  So for many situations you don’t have to
deal with that problem.</p>
<p>To access parameters submitted in the URL (<code class="docutils literal notranslate"><span class="pre">?key=value</span></code>) you can use the
<a class="reference internal" href="../api/#flask.Request.args" title="flask.Request.args"><code class="xref py py-attr docutils literal notranslate"><span class="pre">args</span></code></a> attribute:</p>
<div class="highlight-default notranslate"><div class="highlight"><pre><span></span><span class="n">searchword</span> <span class="o">=</span> <span class="n">request</span><span class="o">.</span><span class="n">args</span><span class="o">.</span><span class="n">get</span><span class="p">(</span><span class="s1">'key'</span><span class="p">,</span> <span class="s1">''</span><span class="p">)</span>
</pre></div>
</div>
<p>We recommend accessing URL parameters with <cite>get</cite> or by catching the
<a class="reference external" href="https://docs.python.org/3/library/exceptions.html#KeyError" title="(in Python v3.10)"><code class="xref py py-exc docutils literal notranslate"><span class="pre">KeyError</span></code></a> because users might change the URL and presenting them a 400
bad request page in that case is not user friendly.</p>
<p>For a full list of methods and attributes of the request object, head over
to the <a class="reference internal" href="../api/#flask.Request" title="flask.Request"><code class="xref py py-class docutils literal notranslate"><span class="pre">Request</span></code></a> documentation.</p>
</section>
<section id="file-uploads">
<h3>File Uploads<a class="headerlink" href="#file-uploads" title="Permalink to this headline">¶</a></h3>
<p>You can handle uploaded files with Flask easily.  Just make sure not to
forget to set the <code class="docutils literal notranslate"><span class="pre">enctype="multipart/form-data"</span></code> attribute on your HTML
form, otherwise the browser will not transmit your files at all.</p>
<p>Uploaded files are stored in memory or at a temporary location on the
filesystem.  You can access those files by looking at the
<code class="xref py py-attr docutils literal notranslate"><span class="pre">files</span></code> attribute on the request object.  Each
uploaded file is stored in that dictionary.  It behaves just like a
standard Python <code class="xref py py-class docutils literal notranslate"><span class="pre">file</span></code> object, but it also has a
<a class="reference external" href="https://werkzeug.palletsprojects.com/en/2.2.x/datastructures/#werkzeug.datastructures.FileStorage.save" title="(in Werkzeug v2.2.x)"><code class="xref py py-meth docutils literal notranslate"><span class="pre">save()</span></code></a> method that
allows you to store that file on the filesystem of the server.
Here is a simple example showing how that works:</p>
<div class="highlight-default notranslate"><div class="highlight"><pre><span></span><span class="kn">from</span> <span class="nn">flask</span> <span class="kn">import</span> <span class="n">request</span>
<span class="nd">@app</span><span class="o">.</span><span class="n">route</span><span class="p">(</span><span class="s1">'/upload'</span><span class="p">,</span> <span class="n">methods</span><span class="o">=</span><span class="p">[</span><span class="s1">'GET'</span><span class="p">,</span> <span class="s1">'POST'</span><span class="p">])</span>
<span class="k">def</span> <span class="nf">upload_file</span><span class="p">():</span>
    <span class="k">if</span> <span class="n">request</span><span class="o">.</span><span class="n">method</span> <span class="o">==</span> <span class="s1">'POST'</span><span class="p">:</span>
        <span class="n">f</span> <span class="o">=</span> <span class="n">request</span><span class="o">.</span><span class="n">files</span><span class="p">[</span><span class="s1">'the_file'</span><span class="p">]</span>
        <span class="n">f</span><span class="o">.</span><span class="n">save</span><span class="p">(</span><span class="s1">'/var/www/uploads/uploaded_file.txt'</span><span class="p">)</span>
    <span class="o">...</span>
</pre></div>
</div>
<p>If you want to know how the file was named on the client before it was
uploaded to your application, you can access the
<a class="reference external" href="https://werkzeug.palletsprojects.com/en/2.2.x/datastructures/#werkzeug.datastructures.FileStorage.filename" title="(in Werkzeug v2.2.x)"><code class="xref py py-attr docutils literal notranslate"><span class="pre">filename</span></code></a> attribute.
However please keep in mind that this value can be forged
so never ever trust that value.  If you want to use the filename
of the client to store the file on the server, pass it through the
<a class="reference external" href="https://werkzeug.palletsprojects.com/en/2.2.x/utils/#werkzeug.utils.secure_filename" title="(in Werkzeug v2.2.x)"><code class="xref py py-func docutils literal notranslate"><span class="pre">secure_filename()</span></code></a> function that
Werkzeug provides for you:</p>
<div class="highlight-default notranslate"><div class="highlight"><pre><span></span><span class="kn">from</span> <span class="nn">werkzeug.utils</span> <span class="kn">import</span> <span class="n">secure_filename</span>
<span class="nd">@app</span><span class="o">.</span><span class="n">route</span><span class="p">(</span><span class="s1">'/upload'</span><span class="p">,</span> <span class="n">methods</span><span class="o">=</span><span class="p">[</span><span class="s1">'GET'</span><span class="p">,</span> <span class="s1">'POST'</span><span class="p">])</span>
<span class="k">def</span> <span class="nf">upload_file</span><span class="p">():</span>
    <span class="k">if</span> <span class="n">request</span><span class="o">.</span><span class="n">method</span> <span class="o">==</span> <span class="s1">'POST'</span><span class="p">:</span>
        <span class="n">file</span> <span class="o">=</span> <span class="n">request</span><span class="o">.</span><span class="n">files</span><span class="p">[</span><span class="s1">'the_file'</span><span class="p">]</span>
        <span class="n">file</span><span class="o">.</span><span class="n">save</span><span class="p">(</span><span class="sa">f</span><span class="s2">"/var/www/uploads/</span><span class="si">{</span><span class="n">secure_filename</span><span class="p">(</span><span class="n">file</span><span class="o">.</span><span class="n">filename</span><span class="p">)</span><span class="si">}</span><span class="s2">"</span><span class="p">)</span>
    <span class="o">...</span>
</pre></div>
</div>
<p>For some better examples, see <a class="reference internal" href="../patterns/fileuploads/"><span class="doc">Uploading Files</span></a>.</p>
</section>
<section id="cookies">
<h3>Cookies<a class="headerlink" href="#cookies" title="Permalink to this headline">¶</a></h3>
<p>To access cookies you can use the <a class="reference internal" href="../api/#flask.Request.cookies" title="flask.Request.cookies"><code class="xref py py-attr docutils literal notranslate"><span class="pre">cookies</span></code></a>
attribute.  To set cookies you can use the
<a class="reference internal" href="../api/#flask.Response.set_cookie" title="flask.Response.set_cookie"><code class="xref py py-attr docutils literal notranslate"><span class="pre">set_cookie</span></code></a> method of response objects.  The
<a class="reference internal" href="../api/#flask.Request.cookies" title="flask.Request.cookies"><code class="xref py py-attr docutils literal notranslate"><span class="pre">cookies</span></code></a> attribute of request objects is a
dictionary with all the cookies the client transmits.  If you want to use
sessions, do not use the cookies directly but instead use the
<a class="reference internal" href="#sessions"><span class="std std-ref">Sessions</span></a> in Flask that add some security on top of cookies for you.</p>
<p>Reading cookies:</p>
<div class="highlight-default notranslate"><div class="highlight"><pre><span></span><span class="kn">from</span> <span class="nn">flask</span> <span class="kn">import</span> <span class="n">request</span>
<span class="nd">@app</span><span class="o">.</span><span class="n">route</span><span class="p">(</span><span class="s1">'/'</span><span class="p">)</span>
<span class="k">def</span> <span class="nf">index</span><span class="p">():</span>
    <span class="n">username</span> <span class="o">=</span> <span class="n">request</span><span class="o">.</span><span class="n">cookies</span><span class="o">.</span><span class="n">get</span><span class="p">(</span><span class="s1">'username'</span><span class="p">)</span>
    <span class="c1"># use cookies.get(key) instead of cookies[key] to not get a</span>
    <span class="c1"># KeyError if the cookie is missing.</span>
</pre></div>
</div>
<p>Storing cookies:</p>
<div class="highlight-default notranslate"><div class="highlight"><pre><span></span><span class="kn">from</span> <span class="nn">flask</span> <span class="kn">import</span> <span class="n">make_response</span>
<span class="nd">@app</span><span class="o">.</span><span class="n">route</span><span class="p">(</span><span class="s1">'/'</span><span class="p">)</span>
<span class="k">def</span> <span class="nf">index</span><span class="p">():</span>
    <span class="n">resp</span> <span class="o">=</span> <span class="n">make_response</span><span class="p">(</span><span class="n">render_template</span><span class="p">(</span><span class="o">...</span><span class="p">))</span>
    <span class="n">resp</span><span class="o">.</span><span class="n">set_cookie</span><span class="p">(</span><span class="s1">'username'</span><span class="p">,</span> <span class="s1">'the username'</span><span class="p">)</span>
    <span class="k">return</span> <span class="n">resp</span>
</pre></div>
</div>
<p>Note that cookies are set on response objects.  Since you normally
just return strings from the view functions Flask will convert them into
response objects for you.  If you explicitly want to do that you can use
the <a class="reference internal" href="../api/#flask.make_response" title="flask.make_response"><code class="xref py py-meth docutils literal notranslate"><span class="pre">make_response()</span></code></a> function and then modify it.</p>
<p>Sometimes you might want to set a cookie at a point where the response
object does not exist yet.  This is possible by utilizing the
<a class="reference internal" href="../patterns/deferredcallbacks/"><span class="doc">Deferred Request Callbacks</span></a> pattern.</p>
<p>For this also see <a class="reference internal" href="#about-responses"><span class="std std-ref">About Responses</span></a>.</p>
</section>
</section>
<section id="redirects-and-errors">
<h2>Redirects and Errors<a class="headerlink" href="#redirects-and-errors" title="Permalink to this headline">¶</a></h2>
<p>To redirect a user to another endpoint, use the <a class="reference internal" href="../api/#flask.redirect" title="flask.redirect"><code class="xref py py-func docutils literal notranslate"><span class="pre">redirect()</span></code></a>
function; to abort a request early with an error code, use the
<a class="reference internal" href="../api/#flask.abort" title="flask.abort"><code class="xref py py-func docutils literal notranslate"><span class="pre">abort()</span></code></a> function:</p>
<div class="highlight-default notranslate"><div class="highlight"><pre><span></span><span class="kn">from</span> <span class="nn">flask</span> <span class="kn">import</span> <span class="n">abort</span><span class="p">,</span> <span class="n">redirect</span><span class="p">,</span> <span class="n">url_for</span>
<span class="nd">@app</span><span class="o">.</span><span class="n">route</span><span class="p">(</span><span class="s1">'/'</span><span class="p">)</span>
<span class="k">def</span> <span class="nf">index</span><span class="p">():</span>
    <span class="k">return</span> <span class="n">redirect</span><span class="p">(</span><span class="n">url_for</span><span class="p">(</span><span class="s1">'login'</span><span class="p">))</span>
<span class="nd">@app</span><span class="o">.</span><span class="n">route</span><span class="p">(</span><span class="s1">'/login'</span><span class="p">)</span>
<span class="k">def</span> <span class="nf">login</span><span class="p">():</span>
    <span class="n">abort</span><span class="p">(</span><span class="mi">401</span><span class="p">)</span>
    <span class="n">this_is_never_executed</span><span class="p">()</span>
</pre></div>
</div>
<p>This is a rather pointless example because a user will be redirected from
the index to a page they cannot access (401 means access denied) but it
shows how that works.</p>
<p>By default a black and white error page is shown for each error code.  If
you want to customize the error page, you can use the
<a class="reference internal" href="../api/#flask.Flask.errorhandler" title="flask.Flask.errorhandler"><code class="xref py py-meth docutils literal notranslate"><span class="pre">errorhandler()</span></code></a> decorator:</p>
<div class="highlight-default notranslate"><div class="highlight"><pre><span></span><span class="kn">from</span> <span class="nn">flask</span> <span class="kn">import</span> <span class="n">render_template</span>
<span class="nd">@app</span><span class="o">.</span><span class="n">errorhandler</span><span class="p">(</span><span class="mi">404</span><span class="p">)</span>
<span class="k">def</span> <span class="nf">page_not_found</span><span class="p">(</span><span class="n">error</span><span class="p">):</span>
    <span class="k">return</span> <span class="n">render_template</span><span class="p">(</span><span class="s1">'page_not_found.html'</span><span class="p">),</span> <span class="mi">404</span>
</pre></div>
</div>
<p>Note the <code class="docutils literal notranslate"><span class="pre">404</span></code> after the <a class="reference internal" href="../api/#flask.render_template" title="flask.render_template"><code class="xref py py-func docutils literal notranslate"><span class="pre">render_template()</span></code></a> call.  This
tells Flask that the status code of that page should be 404 which means
not found.  By default 200 is assumed which translates to: all went well.</p>
<p>See <a class="reference internal" href="../errorhandling/"><span class="doc">Handling Application Errors</span></a> for more details.</p>
</section>
<section id="about-responses">
<span id="id5"></span><h2>About Responses<a class="headerlink" href="#about-responses" title="Permalink to this headline">¶</a></h2>
<p>The return value from a view function is automatically converted into
a response object for you. If the return value is a string it’s
converted into a response object with the string as response body, a
<code class="docutils literal notranslate"><span class="pre">200</span> <span class="pre">OK</span></code> status code and a <em class="mimetype">text/html</em> mimetype. If the
return value is a dict or list, <code class="xref py py-func docutils literal notranslate"><span class="pre">jsonify()</span></code> is called to produce a
response. The logic that Flask applies to converting return values into
response objects is as follows:</p>
<ol class="arabic simple">
<li><p>If a response object of the correct type is returned it’s directly
returned from the view.</p></li>
<li><p>If it’s a string, a response object is created with that data and
the default parameters.</p></li>
<li><p>If it’s an iterator or generator returning strings or bytes, it is
treated as a streaming response.</p></li>
<li><p>If it’s a dict or list, a response object is created using
<a class="reference internal" href="../api/#flask.json.jsonify" title="flask.json.jsonify"><code class="xref py py-func docutils literal notranslate"><span class="pre">jsonify()</span></code></a>.</p></li>
<li><p>If a tuple is returned the items in the tuple can provide extra
information. Such tuples have to be in the form
<code class="docutils literal notranslate"><span class="pre">(response,</span> <span class="pre">status)</span></code>, <code class="docutils literal notranslate"><span class="pre">(response,</span> <span class="pre">headers)</span></code>, or
<code class="docutils literal notranslate"><span class="pre">(response,</span> <span class="pre">status,</span> <span class="pre">headers)</span></code>. The <code class="docutils literal notranslate"><span class="pre">status</span></code> value will override
the status code and <code class="docutils literal notranslate"><span class="pre">headers</span></code> can be a list or dictionary of
additional header values.</p></li>
<li><p>If none of that works, Flask will assume the return value is a
valid WSGI application and convert that into a response object.</p></li>
</ol>
<p>If you want to get hold of the resulting response object inside the view
you can use the <a class="reference internal" href="../api/#flask.make_response" title="flask.make_response"><code class="xref py py-func docutils literal notranslate"><span class="pre">make_response()</span></code></a> function.</p>
<p>Imagine you have a view like this:</p>
<div class="highlight-default notranslate"><div class="highlight"><pre><span></span><span class="kn">from</span> <span class="nn">flask</span> <span class="kn">import</span> <span class="n">render_template</span>
<span class="nd">@app</span><span class="o">.</span><span class="n">errorhandler</span><span class="p">(</span><span class="mi">404</span><span class="p">)</span>
<span class="k">def</span> <span class="nf">not_found</span><span class="p">(</span><span class="n">error</span><span class="p">):</span>
    <span class="k">return</span> <span class="n">render_template</span><span class="p">(</span><span class="s1">'error.html'</span><span class="p">),</span> <span class="mi">404</span>
</pre></div>
</div>
<p>You just need to wrap the return expression with
<a class="reference internal" href="../api/#flask.make_response" title="flask.make_response"><code class="xref py py-func docutils literal notranslate"><span class="pre">make_response()</span></code></a> and get the response object to modify it, then
return it:</p>
<div class="highlight-default notranslate"><div class="highlight"><pre><span></span><span class="kn">from</span> <span class="nn">flask</span> <span class="kn">import</span> <span class="n">make_response</span>
<span class="nd">@app</span><span class="o">.</span><span class="n">errorhandler</span><span class="p">(</span><span class="mi">404</span><span class="p">)</span>
<span class="k">def</span> <span class="nf">not_found</span><span class="p">(</span><span class="n">error</span><span class="p">):</span>
    <span class="n">resp</span> <span class="o">=</span> <span class="n">make_response</span><span class="p">(</span><span class="n">render_template</span><span class="p">(</span><span class="s1">'error.html'</span><span class="p">),</span> <span class="mi">404</span><span class="p">)</span>
    <span class="n">resp</span><span class="o">.</span><span class="n">headers</span><span class="p">[</span><span class="s1">'X-Something'</span><span class="p">]</span> <span class="o">=</span> <span class="s1">'A value'</span>
    <span class="k">return</span> <span class="n">resp</span>
</pre></div>
</div>
<section id="apis-with-json">
<h3>APIs with JSON<a class="headerlink" href="#apis-with-json" title="Permalink to this headline">¶</a></h3>
<p>A common response format when writing an API is JSON. It’s easy to get
started writing such an API with Flask. If you return a <code class="docutils literal notranslate"><span class="pre">dict</span></code> or
<code class="docutils literal notranslate"><span class="pre">list</span></code> from a view, it will be converted to a JSON response.</p>
<div class="highlight-python notranslate"><div class="highlight"><pre><span></span><span class="nd">@app</span><span class="o">.</span><span class="n">route</span><span class="p">(</span><span class="s2">"/me"</span><span class="p">)</span>
<span class="k">def</span> <span class="nf">me_api</span><span class="p">():</span>
    <span class="n">user</span> <span class="o">=</span> <span class="n">get_current_user</span><span class="p">()</span>
    <span class="k">return</span> <span class="p">{</span>
        <span class="s2">"username"</span><span class="p">:</span> <span class="n">user</span><span class="o">.</span><span class="n">username</span><span class="p">,</span>
        <span class="s2">"theme"</span><span class="p">:</span> <span class="n">user</span><span class="o">.</span><span class="n">theme</span><span class="p">,</span>
        <span class="s2">"image"</span><span class="p">:</span> <span class="n">url_for</span><span class="p">(</span><span class="s2">"user_image"</span><span class="p">,</span> <span class="n">filename</span><span class="o">=</span><span class="n">user</span><span class="o">.</span><span class="n">image</span><span class="p">),</span>
    <span class="p">}</span>
<span class="nd">@app</span><span class="o">.</span><span class="n">route</span><span class="p">(</span><span class="s2">"/users"</span><span class="p">)</span>
<span class="k">def</span> <span class="nf">users_api</span><span class="p">():</span>
    <span class="n">users</span> <span class="o">=</span> <span class="n">get_all_users</span><span class="p">()</span>
    <span class="k">return</span> <span class="p">[</span><span class="n">user</span><span class="o">.</span><span class="n">to_json</span><span class="p">()</span> <span class="k">for</span> <span class="n">user</span> <span class="ow">in</span> <span class="n">users</span><span class="p">]</span>
</pre></div>
</div>
<p>This is a shortcut to passing the data to the
<a class="reference internal" href="../api/#flask.json.jsonify" title="flask.json.jsonify"><code class="xref py py-func docutils literal notranslate"><span class="pre">jsonify()</span></code></a> function, which will serialize any supported
JSON data type. That means that all the data in the dict or list must be
JSON serializable.</p>
<p>For complex types such as database models, you’ll want to use a
serialization library to convert the data to valid JSON types first.
There are many serialization libraries and Flask API extensions
maintained by the community that support more complex applications.</p>
</section>
</section>
<section id="sessions">
<span id="id6"></span><h2>Sessions<a class="headerlink" href="#sessions" title="Permalink to this headline">¶</a></h2>
<p>In addition to the request object there is also a second object called
<a class="reference internal" href="../api/#flask.session" title="flask.session"><code class="xref py py-class docutils literal notranslate"><span class="pre">session</span></code></a> which allows you to store information specific to a
user from one request to the next.  This is implemented on top of cookies
for you and signs the cookies cryptographically.  What this means is that
the user could look at the contents of your cookie but not modify it,
unless they know the secret key used for signing.</p>
<p>In order to use sessions you have to set a secret key.  Here is how
sessions work:</p>
<div class="highlight-default notranslate"><div class="highlight"><pre><span></span><span class="kn">from</span> <span class="nn">flask</span> <span class="kn">import</span> <span class="n">session</span>
<span class="c1"># Set the secret key to some random bytes. Keep this really secret!</span>
<span class="n">app</span><span class="o">.</span><span class="n">secret_key</span> <span class="o">=</span> <span class="sa">b</span><span class="s1">'_5#y2L"F4Q8z</span><span class="se">\n\xec</span><span class="s1">]/'</span>
<span class="nd">@app</span><span class="o">.</span><span class="n">route</span><span class="p">(</span><span class="s1">'/'</span><span class="p">)</span>
<span class="k">def</span> <span class="nf">index</span><span class="p">():</span>
    <span class="k">if</span> <span class="s1">'username'</span> <span class="ow">in</span> <span class="n">session</span><span class="p">:</span>
        <span class="k">return</span> <span class="sa">f</span><span class="s1">'Logged in as </span><span class="si">{</span><span class="n">session</span><span class="p">[</span><span class="s2">"username"</span><span class="p">]</span><span class="si">}</span><span class="s1">'</span>
    <span class="k">return</span> <span class="s1">'You are not logged in'</span>
<span class="nd">@app</span><span class="o">.</span><span class="n">route</span><span class="p">(</span><span class="s1">'/login'</span><span class="p">,</span> <span class="n">methods</span><span class="o">=</span><span class="p">[</span><span class="s1">'GET'</span><span class="p">,</span> <span class="s1">'POST'</span><span class="p">])</span>
<span class="k">def</span> <span class="nf">login</span><span class="p">():</span>
    <span class="k">if</span> <span class="n">request</span><span class="o">.</span><span class="n">method</span> <span class="o">==</span> <span class="s1">'POST'</span><span class="p">:</span>
        <span class="n">session</span><span class="p">[</span><span class="s1">'username'</span><span class="p">]</span> <span class="o">=</span> <span class="n">request</span><span class="o">.</span><span class="n">form</span><span class="p">[</span><span class="s1">'username'</span><span class="p">]</span>
        <span class="k">return</span> <span class="n">redirect</span><span class="p">(</span><span class="n">url_for</span><span class="p">(</span><span class="s1">'index'</span><span class="p">))</span>
    <span class="k">return</span> <span class="s1">''' + """'''""" + '''</span>
<span class="s1">        &lt;form method="post"&gt;</span>
<span class="s1">            &lt;p&gt;&lt;input type=text name=username&gt;</span>
<span class="s1">            &lt;p&gt;&lt;input type=submit value=Login&gt;</span>
<span class="s1">        &lt;/form&gt;</span>
<span class="s1">    ''' + """'''""" + '''</span>
<span class="nd">@app</span><span class="o">.</span><span class="n">route</span><span class="p">(</span><span class="s1">'/logout'</span><span class="p">)</span>
<span class="k">def</span> <span class="nf">logout</span><span class="p">():</span>
    <span class="c1"># remove the username from the session if it's there</span>
    <span class="n">session</span><span class="o">.</span><span class="n">pop</span><span class="p">(</span><span class="s1">'username'</span><span class="p">,</span> <span class="kc">None</span><span class="p">)</span>
    <span class="k">return</span> <span class="n">redirect</span><span class="p">(</span><span class="n">url_for</span><span class="p">(</span><span class="s1">'index'</span><span class="p">))</span>
</pre></div>
</div>
<div class="admonition-how-to-generate-good-secret-keys admonition">
<p class="admonition-title">How to generate good secret keys</p>
<p>A secret key should be as random as possible. Your operating system has
ways to generate pretty random data based on a cryptographic random
generator. Use the following command to quickly generate a value for
<code class="xref py py-attr docutils literal notranslate"><span class="pre">Flask.secret_key</span></code> (or <a class="reference internal" href="../config/#SECRET_KEY" title="SECRET_KEY"><code class="xref py py-data docutils literal notranslate"><span class="pre">SECRET_KEY</span></code></a>):</p>
<div class="highlight-default notranslate"><div class="highlight"><pre><span></span>$ python -c 'import secrets; print(secrets.token_hex())'
'192b9bdd22ab9ed4d12e236c78afcb9a393ec15f71bbf5dc987d54727823bcbf'
</pre></div>
</div>
</div>
<p>A note on cookie-based sessions: Flask will take the values you put into the
session object and serialize them into a cookie.  If you are finding some
values do not persist across requests, cookies are indeed enabled, and you are
not getting a clear error message, check the size of the cookie in your page
responses compared to the size supported by web browsers.</p>
<p>Besides the default client-side based sessions, if you want to handle
sessions on the server-side instead, there are several
Flask extensions that support this.</p>
</section>
<section id="message-flashing">
<h2>Message Flashing<a class="headerlink" href="#message-flashing" title="Permalink to this headline">¶</a></h2>
<p>Good applications and user interfaces are all about feedback.  If the user
does not get enough feedback they will probably end up hating the
application.  Flask provides a really simple way to give feedback to a
user with the flashing system.  The flashing system basically makes it
possible to record a message at the end of a request and access it on the next
(and only the next) request.  This is usually combined with a layout
template to expose the message.</p>
<p>To flash a message use the <a class="reference internal" href="../api/#flask.flash" title="flask.flash"><code class="xref py py-func docutils literal notranslate"><span class="pre">flash()</span></code></a> method, to get hold of the
messages you can use <a class="reference internal" href="../api/#flask.get_flashed_messages" title="flask.get_flashed_messages"><code class="xref py py-func docutils literal notranslate"><span class="pre">get_flashed_messages()</span></code></a> which is also
available in the templates. See <a class="reference internal" href="../patterns/flashing/"><span class="doc">Message Flashing</span></a> for a full
example.</p>
</section>
<section id="logging">
<h2>Logging<a class="headerlink" href="#logging" title="Permalink to this headline">¶</a></h2>
<details class="changelog">
<summary>Changelog</summary><div class="versionadded">
<p><span class="versionmodified added">New in version 0.3.</span></p>
</div>
</details><p>Sometimes you might be in a situation where you deal with data that
should be correct, but actually is not.  For example you may have
some client-side code that sends an HTTP request to the server
but it’s obviously malformed.  This might be caused by a user tampering
with the data, or the client code failing.  Most of the time it’s okay
to reply with <code class="docutils literal notranslate"><span class="pre">400</span> <span class="pre">Bad</span> <span class="pre">Request</span></code> in that situation, but sometimes
that won’t do and the code has to continue working.</p>
<p>You may still want to log that something fishy happened.  This is where
loggers come in handy.  As of Flask 0.3 a logger is preconfigured for you
to use.</p>
<p>Here are some example log calls:</p>
<div class="highlight-default notranslate"><div class="highlight"><pre><span></span><span class="n">app</span><span class="o">.</span><span class="n">logger</span><span class="o">.</span><span class="n">debug</span><span class="p">(</span><span class="s1">'A value for debugging'</span><span class="p">)</span>
<span class="n">app</span><span class="o">.</span><span class="n">logger</span><span class="o">.</span><span class="n">warning</span><span class="p">(</span><span class="s1">'A warning occurred (</span><span class="si">%d</span><span class="s1"> apples)'</span><span class="p">,</span> <span class="mi">42</span><span class="p">)</span>
<span class="n">app</span><span class="o">.</span><span class="n">logger</span><span class="o">.</span><span class="n">error</span><span class="p">(</span><span class="s1">'An error occurred'</span><span class="p">)</span>
</pre></div>
</div>
<p>The attached <a class="reference internal" href="../api/#flask.Flask.logger" title="flask.Flask.logger"><code class="xref py py-attr docutils literal notranslate"><span class="pre">logger</span></code></a> is a standard logging
<a class="reference external" href="https://docs.python.org/3/library/logging.html#logging.Logger" title="(in Python v3.10)"><code class="xref py py-class docutils literal notranslate"><span class="pre">Logger</span></code></a>, so head over to the official <a class="reference external" href="https://docs.python.org/3/library/logging.html#module-logging" title="(in Python v3.10)"><code class="xref py py-mod docutils literal notranslate"><span class="pre">logging</span></code></a>
docs for more information.</p>
<p>See <a class="reference internal" href="../errorhandling/"><span class="doc">Handling Application Errors</span></a>.</p>
</section>
<section id="hooking-in-wsgi-middleware">
<h2>Hooking in WSGI Middleware<a class="headerlink" href="#hooking-in-wsgi-middleware" title="Permalink to this headline">¶</a></h2>
<p>To add WSGI middleware to your Flask application, wrap the application’s
<code class="docutils literal notranslate"><span class="pre">wsgi_app</span></code> attribute. For example, to apply Werkzeug’s
<a class="reference external" href="https://werkzeug.palletsprojects.com/en/2.2.x/middleware/proxy_fix/#werkzeug.middleware.proxy_fix.ProxyFix" title="(in Werkzeug v2.2.x)"><code class="xref py py-class docutils literal notranslate"><span class="pre">ProxyFix</span></code></a> middleware for running
behind Nginx:</p>
<div class="highlight-python notranslate"><div class="highlight"><pre><span></span><span class="kn">from</span> <span class="nn">werkzeug.middleware.proxy_fix</span> <span class="kn">import</span> <span class="n">ProxyFix</span>
<span class="n">app</span><span class="o">.</span><span class="n">wsgi_app</span> <span class="o">=</span> <span class="n">ProxyFix</span><span class="p">(</span><span class="n">app</span><span class="o">.</span><span class="n">wsgi_app</span><span class="p">)</span>
</pre></div>
</div>
<p>Wrapping <code class="docutils literal notranslate"><span class="pre">app.wsgi_app</span></code> instead of <code class="docutils literal notranslate"><span class="pre">app</span></code> means that <code class="docutils literal notranslate"><span class="pre">app</span></code> still
points at your Flask application, not at the middleware, so you can
continue to use and configure <code class="docutils literal notranslate"><span class="pre">app</span></code> directly.</p>
</section>
<section id="using-flask-extensions">
<h2>Using Flask Extensions<a class="headerlink" href="#using-flask-extensions" title="Permalink to this headline">¶</a></h2>
<p>Extensions are packages that help you accomplish common tasks. For
example, Flask-SQLAlchemy provides SQLAlchemy support that makes it simple
and easy to use with Flask.</p>
<p>For more on Flask extensions, see <a class="reference internal" href="../extensions/"><span class="doc">Extensions</span></a>.</p>
</section>
<section id="deploying-to-a-web-server">
<h2>Deploying to a Web Server<a class="headerlink" href="#deploying-to-a-web-server" title="Permalink to this headline">¶</a></h2>
<p>Ready to deploy your new Flask app? See <a class="reference internal" href="../deploying/"><span class="doc">Deploying to Production</span></a>.</p>
</section>
</section>
            <div class="clearer"></div>
          <div id="rtd-sidebar" data-ea-publisher="readthedocs-pallets" data-ea-type="readthedocs-sidebar" data-ea-manual="true" class="ethical-alabaster" data-ea-keywords="flask|jinja|python|readthedocs-project-96|readthedocs-project-flask|web-framework|werkzeug|wsgi" data-ea-campaign-types="community|house|paid"></div></div>
        </div>
      </div>
  <span id="sidebar-top"></span>
      <div class="sphinxsidebar" role="navigation" aria-label="main navigation">
        <div class="sphinxsidebarwrapper">
            <p class="logo"><a href="../">
              <img class="logo" src="../_static/flask-icon.png" alt="Logo">
            </a></p>
  <h3>Contents</h3>
  <ul>
<li><a class="reference internal" href="#">Quickstart</a><ul>
<li><a class="reference internal" href="#a-minimal-application">A Minimal Application</a></li>
<li><a class="reference internal" href="#debug-mode">Debug Mode</a></li>
<li><a class="reference internal" href="#html-escaping">HTML Escaping</a></li>
<li><a class="reference internal" href="#routing">Routing</a><ul>
<li><a class="reference internal" href="#variable-rules">Variable Rules</a></li>
<li><a class="reference internal" href="#unique-urls-redirection-behavior">Unique URLs / Redirection Behavior</a></li>
<li><a class="reference internal" href="#url-building">URL Building</a></li>
<li><a class="reference internal" href="#http-methods">HTTP Methods</a></li>
</ul>
</li>
<li><a class="reference internal" href="#static-files">Static Files</a></li>
<li><a class="reference internal" href="#rendering-templates">Rendering Templates</a></li>
<li><a class="reference internal" href="#accessing-request-data">Accessing Request Data</a><ul>
<li><a class="reference internal" href="#context-locals">Context Locals</a></li>
<li><a class="reference internal" href="#the-request-object">The Request Object</a></li>
<li><a class="reference internal" href="#file-uploads">File Uploads</a></li>
<li><a class="reference internal" href="#cookies">Cookies</a></li>
</ul>
</li>
<li><a class="reference internal" href="#redirects-and-errors">Redirects and Errors</a></li>
<li><a class="reference internal" href="#about-responses">About Responses</a><ul>
<li><a class="reference internal" href="#apis-with-json">APIs with JSON</a></li>
</ul>
</li>
<li><a class="reference internal" href="#sessions">Sessions</a></li>
<li><a class="reference internal" href="#message-flashing">Message Flashing</a></li>
<li><a class="reference internal" href="#logging">Logging</a></li>
<li><a class="reference internal" href="#hooking-in-wsgi-middleware">Hooking in WSGI Middleware</a></li>
<li><a class="reference internal" href="#using-flask-extensions">Using Flask Extensions</a></li>
<li><a class="reference internal" href="#deploying-to-a-web-server">Deploying to a Web Server</a></li>
</ul>
</li>
</ul>
<h3>Navigation</h3>
<ul>
  <li><a href="../">Overview</a>
    <ul>
          <li>Previous: <a href="../installation/" title="previous chapter">Installation</a>
          </li><li>Next: <a href="../tutorial/" title="next chapter">Tutorial</a>
    </li></ul>
  </li>
</ul>
<div id="searchbox" style="" role="search">
  <h3 id="searchlabel">Quick search</h3>
    <div class="searchformwrapper">
    <form class="search" action="../search/" method="get">
      <input type="text" name="q" aria-labelledby="searchlabel" autocomplete="off" autocorrect="off" autocapitalize="off" spellcheck="false">
      <input type="submit" value="Go">
    </form>
    </div>
</div>
<script>$('#searchbox').show(0);</script><div id="ethical-ad-placement"></div>
        </div>
      </div>
      <div class="clearer"></div>
    </div>
    <div class="footer" role="contentinfo">
        © Copyright 2010 Pallets.
      Created using <a href="https://www.sphinx-doc.org/">Sphinx</a> 4.5.0.
    </div>
  <script src="../_static/version_warning_offset.js"></script>
<!-- Inserted RTD Footer -->
<div class="injected">
  <div class="rst-versions rst-badge" data-toggle="rst-versions">
    <span class="rst-current-version" data-toggle="rst-current-version">
      <span class="fa fa-book">&nbsp;</span>
      v: latest
      <span class="fa fa-caret-down"></span>
    </span>
    <div class="rst-other-versions">
      <dl>
        <dt>Версии</dt>
        <dd class="rtd-current-item">
          <a href="https://flask.palletsprojects.com/en/latest/quickstart/">latest</a>
        </dd>
        <dd>
          <a href="https://flask.palletsprojects.com/en/2.2.x/quickstart/">2.2.x</a>
        </dd>
        <dd>
          <a href="https://flask.palletsprojects.com/en/2.1.x/quickstart/">2.1.x</a>
        </dd>
        <dd>
          <a href="https://flask.palletsprojects.com/en/2.0.x/quickstart/">2.0.x</a>
        </dd>
        <dd>
          <a href="https://flask.palletsprojects.com/en/1.1.x/quickstart/">1.1.x</a>
        </dd>
        <dd>
          <a href="https://flask.palletsprojects.com/en/1.0.x/quickstart/">1.0.x</a>
        </dd>
        <dd>
          <a href="https://flask.palletsprojects.com/en/0.12.x/quickstart/">0.12.x</a>
        </dd>
      </dl>
      <dl>
        <!-- These are kept as relative links for internal installs that are http -->
        <dt>On Read the Docs</dt>
        <dd>
          <a href="//readthedocs.org/projects/flask/">Project Home</a>
        </dd>
        <dd>
          <a href="//readthedocs.org/projects/flask/builds/">Сборки</a>
        </dd>
        <dd>
          <a href="//readthedocs.org/projects/flask/downloads/">Скачать</a>
        </dd>
      </dl>
      <dl>
        <dt>On GitHub</dt>
        <dd>
          <a href="https://github.com/pallets/flask/blob/main/docs/quickstart.rst">Просмотреть</a>
        </dd>
      </dl>
      <dl>
        <dt>Поиск</dt>
        <dd>
          <div style="padding: 6px;">
            <form id="flyout-search-form" class="wy-form" target="_blank" action="//readthedocs.org/projects/flask/search/" method="get">
              <input type="text" name="q" aria-label="Search docs" placeholder="Search docs">
              </form>
          </div>
        </dd>
      </dl>
      <hr>
        <small>
          <span>Hosted by <a href="https://readthedocs.org">Read the Docs</a></span>
          <span> · </span>
          <a href="https://docs.readthedocs.io/page/privacy-policy.html">Политика приватности</a>
        </small>
    </div>
  </div>
</div>
</body>'''


app.run(debug=True)
