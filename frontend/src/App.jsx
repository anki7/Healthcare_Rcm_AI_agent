import React, { useState, useEffect } from 'react'
import axios from 'axios'

const API_URL = 'https://healthcare-rcm-api.onrender.com'
const api = axios.create({ baseURL: API_URL })

function App() {
  const [status, setStatus] = useState('loading')
  const [patients, setPatients] = useState([])
  const [denials, setDenials] = useState([])

  useEffect(() => {
    fetchData()
  }, [])

  const fetchData = async () => {
    try {
      const health = await api.get('/health')
      setStatus('healthy')
      
      const patientsRes = await api.get('/patients')
      setPatients(patientsRes.data.patients || [])
      
      const denialsRes = await api.get('/denials?limit=10')
      setDenials(denialsRes.data.denials || [])
    } catch (error) {
      setStatus('error')
      console.error('Error:', error)
    }
  }

  return (
    <div style={{ fontFamily: 'Arial, sans-serif', padding: '20px', maxWidth: '800px', margin: '0 auto' }}>
      <header style={{ background: 'linear-gradient(135deg, #667eea 0%, #764ba2 100%)', color: 'white', padding: '20px', borderRadius: '15px', marginBottom: '20px' }}>
        <h1>🏥 Healthcare RCM AI Agent</h1>
        <p>Status: {status === 'healthy' ? '✅ Connected' : '❌ Offline'}</p>
      </header>

      <div style={{ display: 'grid', gridTemplateColumns: '1fr 1fr', gap: '20px' }}>
        <div style={{ background: 'white', padding: '15px', borderRadius: '10px', boxShadow: '0 2px 4px rgba(0,0,0,0.1)' }}>
          <h3>👤 Patients ({patients.length})</h3>
          {patients.map((p, i) => (
            <div key={i} style={{ padding: '8px', borderBottom: '1px solid #eee' }}>
              {p.name} - {p.age} years
            </div>
          ))}
        </div>
        <div style={{ background: 'white', padding: '15px', borderRadius: '10px', boxShadow: '0 2px 4px rgba(0,0,0,0.1)' }}>
          <h3>🚫 Denials ({denials.length})</h3>
          {denials.map((d, i) => (
            <div key={i} style={{ padding: '8px', borderBottom: '1px solid #eee' }}>
              {d.id} - {d.description}
            </div>
          ))}
        </div>
      </div>
    </div>
  )
}

export default App
