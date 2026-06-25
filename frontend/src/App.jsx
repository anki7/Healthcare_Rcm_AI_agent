import React, { useState, useEffect } from 'react'
import axios from 'axios'

const api = axios.create({ baseURL: '/api' })

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
    }
  }

  return (
    <div style={{ fontFamily: 'Arial, sans-serif', padding: '20px', maxWidth: '1200px', margin: '0 auto' }}>
      <header style={{ background: 'linear-gradient(135deg, #667eea, #764ba2)', color: 'white', padding: '20px', borderRadius: '15px', marginBottom: '30px' }}>
        <h1>🏥 Healthcare RCM AI Agent</h1>
        <p>Status: {status === 'healthy' ? '✅ Connected' : '❌ Offline'}</p>
      </header>

      <div style={{ display: 'grid', gridTemplateColumns: 'repeat(3, 1fr)', gap: '20px', marginBottom: '30px' }}>
        <div style={{ background: 'white', padding: '20px', borderRadius: '10px', boxShadow: '0 2px 4px rgba(0,0,0,0.1)' }}>
          <h3>Total Patients</h3>
          <p style={{ fontSize: '24px', fontWeight: 'bold' }}>{patients.length}</p>
        </div>
        <div style={{ background: 'white', padding: '20px', borderRadius: '10px', boxShadow: '0 2px 4px rgba(0,0,0,0.1)' }}>
          <h3>Total Denials</h3>
          <p style={{ fontSize: '24px', fontWeight: 'bold' }}>{denials.length}</p>
        </div>
        <div style={{ background: 'white', padding: '20px', borderRadius: '10px', boxShadow: '0 2px 4px rgba(0,0,0,0.1)' }}>
          <h3>Status</h3>
          <p style={{ fontSize: '24px', fontWeight: 'bold', color: status === 'healthy' ? 'green' : 'red' }}>
            {status === 'healthy' ? '✅ Online' : '❌ Offline'}
          </p>
        </div>
      </div>

      <div style={{ display: 'grid', gridTemplateColumns: '1fr 1fr', gap: '20px' }}>
        <div style={{ background: 'white', padding: '20px', borderRadius: '10px', boxShadow: '0 2px 4px rgba(0,0,0,0.1)' }}>
          <h3>👤 Patients</h3>
          {patients.map((p, i) => (
            <div key={i} style={{ padding: '10px', borderBottom: '1px solid #f0f0f0' }}>
              <strong>{p.name}</strong> - {p.age} years - {p.conditions.join(', ')}
            </div>
          ))}
        </div>
        <div style={{ background: 'white', padding: '20px', borderRadius: '10px', boxShadow: '0 2px 4px rgba(0,0,0,0.1)' }}>
          <h3>🚫 Denials</h3>
          {denials.map((d, i) => (
            <div key={i} style={{ padding: '10px', borderBottom: '1px solid #f0f0f0' }}>
              <strong>{d.id}</strong> - {d.description}
              <span style={{ float: 'right', color: d.priority === 'HIGH' ? 'red' : 'orange' }}>{d.priority}</span>
            </div>
          ))}
        </div>
      </div>
    </div>
  )
}

export default App
