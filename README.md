# McMahon CIM Optimizer (Cornell 大学)

MaxCut 问题的 McMahon CIM Optimizer 测试方法的存储库 (Repository for testing McMahon CIM Optimizer algorithm for MaxCut problem)

<h2> 概述  </h2>
<h3>测试指标 Test metrics</h3>
 
 
 <b>顶点 nodes:</b> 100
 <br>
 <b>边缘密度 edge density:</b> 10%, 30%, 50%, 70%, 90%
 <br><br>
 <b>顶点 nodes:</b> 500
 <br>
 <b>边缘密度 edge density:</b> 10%, 30%, 50%, 70%, 90%
 
 
<h2>测试方法 </h2>
<h3>McMahon Labs CIM Optimizer </h3>
Simulated annealing using the <code>cim-optimizer</code> package<br>

<br>
[repository](https://github.com/mcmahon-lab/cim-optimizer)

 <h2>指示 </h2>
 <h4>克隆此文件夹 Clone this folder</h4>
   <code>git clone</code>

<h4>安装所需的包 Install dependencies</h4>
  <code>pip install cim-optimizer</code> <br>
  <code>pip install -r requirements.txt</code> <br><br>
  <h4>启动测试文件 Launch test files </h4>
  输入 <code>python </code>，然后输入测试文件名  <br>
<br>
比如: <br><br> 
<code>python runTest100_10.py</code>
<br><br>
或:
<br><br>
<code>python runTest500_70.py</code>
